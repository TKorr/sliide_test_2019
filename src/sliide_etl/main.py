#!/usr/bin/env python3
import argparse
import json

import pandas as pd

import src.sliide_etl.utils.logger as logger

LOGGER = logger.set_logger()
DATA_FILE_PATH = "bq-results-sample-data.json"
TEST_DATA_FILE_PATH = "test_data.json"


def print_hello_ea(arg):
    """
    Function to print "Hello, EA! - " + input string
    :return:
    """
    return_statement = "Hello, EA! - {}".format(arg)
    return return_statement


def read_json_data():
    json_data = pd.read_json(DATA_FILE_PATH, )
    pass


def parse_arguments():
    """
    Parser for command-line options, arguments and sub-commands
    Returns:
        parser.parse_args()
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("input_statement", type=str, help="Say something!")
    return parser.parse_args()


def main():
    """
    Main function starts running the script, configures logging and executes script
    Returns:
      None
    """
    # arguments = parse_arguments()
    # json_data = pd.read_json(TEST_DATA_FILE_PATH)
    # read file
    with open(TEST_DATA_FILE_PATH, 'r') as myfile:
        data = myfile.read()

    # parse file
    obj = json.loads(data)
    count = 0

    if obj['event_name'] == 'user_engagement':
        for event_param in obj['event_params']:
            key = event_param['key']
            if key == 'engagement_time_msec' and int(event_param['value']['int_value']) >= 3000:
                for event_param2 in obj['event_params']:
                    key = event_param2['key']
                    if key == 'engaged_session_event' and int(event_param['value']['int_value']) >= 1:
                        count += 1
    print(count)
    # print(obj)


if __name__ == "__main__":  # pragma: no cover
    LOGGER.info("---")
    main()
