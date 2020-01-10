#!/usr/bin/env python3
import argparse
import datetime
import json
import os
import types

import mysql.connector

import src.sliide_etl.utils.logger as logger

LOGGER = logger.set_logger()
HOST = os.environ("hostname"),
USER = os.environ("username"),
PASSWORD = os.environ("password"),
DATABASE = os.environ("database")


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


def count_user_engagement(json_obj: types.GeneratorType) -> int:
    """Function to return the count of active users.

    :param json_obj: types.GeneratorType:
    :return: int
    """

    count = 0
    for event in json_obj:
        if event['event_name'] == 'user_engagement':
            for event_param in event['event_params']:
                key = event_param['key']
                if key == 'engagement_time_msec' and int(event_param['value']['int_value']) >= 3000:
                    for event_param2 in event['event_params']:
                        key = event_param2['key']
                        if key == 'engaged_session_event' and int(event_param['value']['int_value']) >= 1:
                            count += 1
    return count


def load_data_to_table(data):
    date = datetime.datetime.now()
    active_user_count = data

    query = "INSERT INTO active_user_table(date,active_user_count) VALUES(%s,%s)"
    args = (date, active_user_count)

    try:
        mydb = mysql.connector.connect(
            host=HOST,
            user=USER,
            passwd=PASSWORD,
            database=DATABASE
        )
        cursor = mydb.cursor()
        cursor.execute(query, args)
        mydb.commit()
    except ConnectionError as error:
        print(error)

    finally:
        cursor.close()


def main():
    LOGGER.info("---")
    arguments = parse_arguments()
    event_gen = read_json_data(arguments.input_file)
    result = count_user_engagement(event_gen)
    load_data_to_table(result)


if __name__ == "__main__":  # pragma: no cover
    main()
