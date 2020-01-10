#!/usr/bin/env python3
import argparse
import json
import types

import src.sliide_etl.utils.logger as logger

LOGGER = logger.set_logger()


def read_json_data(fp: str) -> types.GeneratorType:
    """

    :param fp:
    :return:
    """
    with open(fp) as f:
        for line in f:
            yield json.loads(line)


def parse_arguments() -> argparse.Namespace:
    """
    Parser for command-line options, arguments and sub-commands
    Returns:
        parser.parse_args()
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", type=str, help="Input file path to data")
    return parser.parse_args()


def count_user_engagement(json_obj: types.GeneratorType) -> int:
    """

    Returns:
      Int count
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


def main() -> None:
    LOGGER.info("Start")
    arguments = parse_arguments()
    event_gen = read_json_data(arguments.input_file)
    result = count_user_engagement(event_gen)
    print(result)


if __name__ == "__main__":  # pragma: no cover
    main()
