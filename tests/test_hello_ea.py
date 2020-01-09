import argparse

import pytest
from __name__ import hello_ea


def test_print_hello_ea():
    assert hello_ea.print_hello_ea("testing"), "Hello, EA! - testing"


@pytest.fixture
def create_parser():
    parser = hello_ea.parse_arguments()
    return parser


def test_parse_arguments(create_parser):
    assert create_parser is not None


def test_parse_arguments_testing(create_parser):
    create_parser.input_statement = "testing"
    expected = argparse.Namespace(input_statement='testing')
    assert create_parser == expected


def test_main():
    assert hello_ea.main() == None
