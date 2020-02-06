from collections import OrderedDict

import pytest

from oarepo_nusl_rules.xoai.rules import xoai_creator


@pytest.fixture
def source():
    return OrderedDict(
        [
            ('@name', 'none'),
            ('field', OrderedDict(
                [
                    ('@name', 'value'),
                    ('#text', 'Rycheva, Ekaterina')
                ]
            )
             )
        ]
    )


def test_creator_1(source):
    assert xoai_creator(source) == {
        'creator':
            [
                {'name': 'Rycheva, Ekaterina'}
            ]
    }
