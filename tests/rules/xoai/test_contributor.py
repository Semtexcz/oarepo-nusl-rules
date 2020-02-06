from collections import OrderedDict

import pytest

from oarepo_nusl_rules.xoai.rules import xoai_contributor


@pytest.fixture
def source():
    return [
        OrderedDict(
            [
                ('@name', 'advisor'),
                ('element', OrderedDict(
                    [
                        ('@name', 'none'),
                        ('field', OrderedDict(
                            [
                                ('@name', 'value'),
                                ('#text', 'Rajnochová, Natalie')
                            ]
                        )
                         )
                    ]
                )
                 )
            ]
        ),
        OrderedDict(
            [
                ('@name', 'referee'),
                ('element', OrderedDict(
                    [
                        ('@name', 'none'),
                        ('field', [
                            OrderedDict(
                                [
                                    ('@name', 'value'),
                                    ('#text', 'Mokienko, Valerij')
                                ]
                            ),
                            OrderedDict(
                                [
                                    ('@name', 'value'),
                                    ('#text', 'Stěpanova, Ludmila')
                                ]
                            )
                        ]
                         )
                    ]
                )
                 )
            ]
        )
    ]


def test_contributor_1(source):
    assert xoai_contributor(source) == {
        "contributor": [{'name': 'Rajnochová, Natalie', 'role': 'advisor'},
                        {'name': 'Mokienko, Valerij', 'role': 'referee'},
                        {'name': 'Stěpanova, Ludmila', 'role': 'referee'}]
    }
