from collections import OrderedDict

import pytest

from oarepo_nusl_rules.xoai.rules import xoai_title


@pytest.fixture
def source_1():
    return [OrderedDict([('@name', 'cs_CZ'),
                         ('field',
                          OrderedDict([('@name', 'value'),
                                       ('#text',
                                        'Reorganizace dle insolvenčního práva')]))]),
            OrderedDict([('@name', 'translated'),
                         ('element',
                          OrderedDict([('@name', 'en_US'),
                                       ('field',
                                        OrderedDict([('@name', 'value'),
                                                     ('#text',
                                                      'Reorganization under insolvency '
                                                      'law')]))]))])]


@pytest.fixture
def source_2():
    return [OrderedDict([('@name', 'de_DE'),
                         ('field',
                          OrderedDict([('@name', 'value'),
                                       ('#text',
                                        'Synagogale Musikpraxis in Prag zur Zeit der '
                                        'Ersten Tschechoslowakischen Republik')]))]),
            OrderedDict([('@name', 'translated'),
                         ('element',
                          [OrderedDict([('@name', 'en_US'),
                                        ('field',
                                         OrderedDict([('@name', 'value'),
                                                      ('#text',
                                                       'Synagogal Music Practice in '
                                                       'Prague at the time of the First '
                                                       'Czechoslovak Republic')]))]),
                           OrderedDict([('@name', 'cs_CZ'),
                                        ('field',
                                         OrderedDict([('@name', 'value'),
                                                      ('#text',
                                                       'Synagogale Musikpraxis in Prag '
                                                       'zur Zeit der Ersten '
                                                       'Tschechoslowakischen '
                                                       'Republik')]))])])])]


@pytest.fixture
def source_3():
    return [OrderedDict([('@name', 'de_DE'),
                         ('field',
                          OrderedDict([('@name', 'value'),
                                       ('#text',
                                        'Gallizismen im Deutschen: eine korpusbasierte '
                                        'Recherche')]))]),
            OrderedDict([('@name', 'translated'),
                         ('element',
                          [OrderedDict([('@name', 'en_US'),
                                        ('field',
                                         OrderedDict([('@name', 'value'),
                                                      ('#text',
                                                       'Gallicisms in German: a '
                                                       'Corpus-Based Study')]))]),
                           OrderedDict([('@name', 'cs_CZ'),
                                        ('field',
                                         OrderedDict([('@name', 'value'),
                                                      ('#text',
                                                       'Galicismy v němčině: korpusová '
                                                       'analýza')]))])])])]


def test_title_1(source_1):
    assert xoai_title(source_1) == {
        'title': [
            {'name': 'Reorganizace dle insolvenčního práva', 'lang': 'cze'},
            {'name': 'Reorganization under insolvency law', 'lang': 'eng'}
        ]
    }


def test_title_2(source_2):
    assert xoai_title(source_2) == {
        'title': [
            {
                'name': 'Synagogale Musikpraxis in Prag zur Zeit der Ersten '
                        'Tschechoslowakischen Republik',
                'lang': 'ger'
            },
            {
                'name': 'Synagogal Music Practice in Prague at the time of the First '
                        'Czechoslovak Republic',
                'lang': 'eng'
            },
            {
                'name': 'Synagogale Musikpraxis in Prag zur Zeit der Ersten Tschechoslowakischen '
                        'Republik',
                'lang': 'cze'
            }
        ]
    }


def test_title_3(source_3):
    assert xoai_title(source_3) == {
        'title': [
            {'name': 'Gallizismen im Deutschen: eine korpusbasierte Recherche', 'lang': 'ger'},
            {'name': 'Gallicisms in German: a Corpus-Based Study', 'lang': 'eng'},
            {'name': 'Galicismy v němčině: korpusová analýza', 'lang': 'cze'}]
    }
