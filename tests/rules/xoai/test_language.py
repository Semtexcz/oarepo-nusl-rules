from collections import OrderedDict

from pytest import fixture

from oarepo_nusl_rules.xoai.rules import xoai_language


@fixture
def source():
    return OrderedDict([('@name', 'none'),
                        ('field', OrderedDict([('@name', 'value'), ('#text', 'cs_CZ')]))])


def test_language_1(source, app, db):
    assert xoai_language(source) == {
        'language': [{'$ref': 'https://localhost/api/taxonomies/languages/cze'}]
    }
