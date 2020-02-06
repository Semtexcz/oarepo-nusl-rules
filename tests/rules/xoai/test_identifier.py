from collections import OrderedDict

from pytest import fixture

from oarepo_nusl_rules.xoai.rules import xoai_identifier


@fixture
def identifier():
    return OrderedDict([('@name', 'none'),
                        ('field',
                         OrderedDict([('@name', 'value'),
                                      ('#text',
                                       'http://hdl.handle.net/20.500.11956/115864')]))])


@fixture
def header_id_oai():
    return 'oai:dspace.cuni.cz:20.500.11956/115864'


def test_identifier_1(identifier, header_id_oai):
    assert xoai_identifier(identifier, identifier=header_id_oai) == {
        'identifier': [{'value': 'oai:dspace.cuni.cz:20.500.11956/115864', 'type': 'originalOAI'}, {
            'value': 'http://hdl.handle.net/20.500.11956/115864', 'type': 'originalRecord'
        }]
    }


def test_identifier_2(identifier):
    assert xoai_identifier(identifier) == {
        'identifier': [{'value': 'oai:dspace.cuni.cz:20.500.11956/115864', 'type': 'originalOAI'}, {
            'value': 'http://hdl.handle.net/20.500.11956/115864', 'type': 'originalRecord'
        }]
    }
