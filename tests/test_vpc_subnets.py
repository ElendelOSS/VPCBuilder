import json
import os

import yaml
from pytest import fixture

from src.newmacro import handler


def _load_resource_as_json(path_under_resources):
    path = os.path.join(os.path.dirname(__file__), 'resources', path_under_resources)

    with open(path) as json_file:
        data = json.load(json_file)
    return data


def _string_to_yaml(string_to_convert):
    return yaml.load(string_to_convert, Loader=yaml.FullLoader)


@fixture
def builder():
    return handler


def test_vpc_builder_subnets(builder, template="vpc_subnets.json"):
    cfn_fragment = _load_resource_as_json(f'request/{template}')
    actual_resources = builder(cfn_fragment, "object")

    expected_resources = _load_resource_as_json(f'response/{template}')
    assert actual_resources == expected_resources