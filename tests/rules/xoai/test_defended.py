from collections import OrderedDict

from pytest import fixture

from oarepo_nusl_rules.xoai.rules import xoai_defended


@fixture
def defended():
    return [OrderedDict([('@name', 'cs'),
                         ('element',
                          OrderedDict([('@name', 'cs_CZ'),
                                       ('field',
                                        OrderedDict([('@name', 'value'),
                                                     ('#text', 'Prospěl/a')]))]))]),
            OrderedDict([('@name', 'en'),
                         ('element',
                          OrderedDict([('@name', 'en_US'),
                                       ('field',
                                        OrderedDict([('@name', 'value'),
                                                     ('#text', 'Pass')]))]))]),
            OrderedDict([('@name', 'code'),
                         ('element',
                          OrderedDict([('@name', 'none'),
                                       ('field',
                                        OrderedDict([('@name', 'value'),
                                                     ('#text', 'P')]))]))])]


@fixture
def not_defended():
    return [OrderedDict([('@name', 'cs'),
                         ('element',
                          OrderedDict([('@name', 'cs_CZ'),
                                       ('field',
                                        OrderedDict([('@name', 'value'),
                                                     ('#text', 'Neprospěl/a')]))]))]),
            OrderedDict([('@name', 'en'),
                         ('element',
                          OrderedDict([('@name', 'en_US'),
                                       ('field',
                                        OrderedDict([('@name', 'value'),
                                                     ('#text', 'Fail')]))]))]),
            OrderedDict([('@name', 'code'),
                         ('element',
                          OrderedDict([('@name', 'none'),
                                       ('field',
                                        OrderedDict([('@name', 'value'),
                                                     ('#text', '4')]))]))])]


def test_defended_1(defended):
    assert xoai_defended(defended) == {'defended': True}


def test_defended_2(not_defended):
    assert xoai_defended(not_defended) == {'defended': False}
