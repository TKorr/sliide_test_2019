#!/usr/bin/env python3
import argparse
import datetime
import json
import types

import sqlalchemy as sa

import src.sliide_etl.utils.logger as logger

LOGGER = logger.set_logger()


# Credentials for database connection
# HOST = os.environ("hostname")
# USER = os.environ("username")
# PASSWORD = os.environ("password")
# DATABASE = os.environ("database")


def read_json_data(fp: str) -> types.GeneratorType:
    """Function to return a generator that be used to iterate through each record.

    :param fp:
    :return: types.GeneratorType
    """
    with open(fp) as f:
        for line in f:
            yield json.loads(line)


def parse_arguments() -> argparse.Namespace:
    """Parser for command-line options, arguments and sub-commands

    :return: parser.parse_args()
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", type=str, help="Input file path to data")
    return parser.parse_args()


def count_user_engagement(json_obj: types.GeneratorType) -> (datetime, int):
    """Function to return the count of active users.

    :param json_obj: types.GeneratorType:
    :return: int
    """
    result = {}
    for event in json_obj:
        if event['event_name'] == 'user_engagement':
            event_date = datetime.datetime.strptime(event['event_date'], "%Y%M%d").strftime("%Y-%M-%d")
            for event_param in event['event_params']:
                key = event_param['key']
                if key == 'engagement_time_msec' and int(event_param['value']['int_value']) >= 3000:
                    for event_param2 in event['event_params']:
                        key = event_param2['key']
                        if key == 'engaged_session_event' and int(event_param['value']['int_value']) >= 1:
                            if event_date in result:
                                result[event_date] += 1
                            else:
                                result[event_date] = 1

    return result


def db_engine():
    engine = sa.create_engine(f"mysql://{USER}:{PASSWORD}@{HOST}/{DATABASE}", echo=True)
    return engine


def create_table():
    metadata = sa.MetaData()
    active_user_table = sa.Table("active_user_table", metadata,
                                 sa.Column("date", sa.DATE),
                                 sa.Column("active_user_count", sa.Integer)
                                 )
    metadata.create_all(db_engine())


def load_data_to_table(data: dict) -> None:
    """Function to load event record data into database.

    :param db_engine:
    :param data: int
    :return: None
    """

    if not db_engine().dialect.has_table(db_engine(), "active_user_table"):
        create_table()

    # Create MetaData instance
    metadata = sa.MetaData(db_engine()).reflect()

    # Get Table
    table = metadata.tables['active_user_table']
    ins = table.insert()

    # Set values into records
    values = [{"date": date, "active_user_count": count} for date, count in data.items()]

    try:
        conn = db_engine().connect()
        conn.execute(ins, values)
        conn.close()
    except ConnectionError as error:
        print(error)
    finally:
        db_engine().dispose()


def main():
    LOGGER.info("---")
    arguments = parse_arguments()
    event_gen = read_json_data(arguments.input_file)
    result = count_user_engagement(event_gen)
    print(result)

    # Load data into database
    # load_data_to_table(result)


if __name__ == "__main__":  # pragma: no cover
    main()
