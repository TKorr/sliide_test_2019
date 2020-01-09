#!/usr/bin/env python3
import argparse

import __name__.utils.logger as logger

LOGGER = logger.set_logger()


def print_hello_ea(arg):
    """
    Function to print "Hello, EA! - " + input string
    :return:
    """
    return_statement = "Hello, EA! - {}".format(arg)
    return return_statement


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
    arguments = parse_arguments()
    print_statement = print_hello_ea(arguments.input_statement)
    print(print_statement)


if __name__ == "__main__":  # pragma: no cover
    LOGGER.info("---")
    main()
