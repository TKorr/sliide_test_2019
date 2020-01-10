import argparse
import types

import pytest

from src.sliide_etl import main


@pytest.fixture
def create_parser():
    parser = main.parse_arguments()
    return parser


def test_parse_arguments(create_parser):
    assert create_parser is not None


def test_parse_arguments_testing(create_parser):
    create_parser.input_statement = "testing"
    expected = argparse.Namespace(input_file='test_sliide_etl.py', input_statement='testing')
    assert create_parser == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("test_data_non_user_engagement_event.json", "push_received"),
        ("test_data_user_engagement_event.json", "user_engagement")
    ]
)
def test_read_json_data(test_input, expected):
    test_event_obj = main.read_json_data(test_input)
    assert isinstance(test_event_obj, types.GeneratorType)
    for event in test_event_obj:
        assert event["event_name"] == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("test_data_non_user_engagement_event.json", 0),
        ("test_data_user_engagement_event.json", 1)
    ]
)
def test_count_engagment_users(test_input, expected):
    test_event_obj = main.read_json_data(test_input)
    assert main.count_user_engagement(test_event_obj) == expected
