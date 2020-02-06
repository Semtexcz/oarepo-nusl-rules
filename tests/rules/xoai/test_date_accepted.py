from collections import OrderedDict

import pytest

from oarepo_nusl_rules.xoai.rules import xoai_date_accepted


@pytest.fixture()
def source():
    return OrderedDict(
        [('@name', 'none'), ('field', OrderedDict([('@name', 'value'), ('#text', '2019-12-19')]))])


def test_date_accepted_1(source):
    assert xoai_date_accepted(source) == {'dateAccepted': '2019-12-19'}
