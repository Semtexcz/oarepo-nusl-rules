from pprint import pprint

from sickle import Sickle

from oarepo_oai_parsers.parsers import XOAIRecord


def get_source(address, identifier: str):
    sickle = Sickle("https://dspace.cuni.cz/oai/nusl")
    sickle.class_mapping['GetRecord'] = XOAIRecord
    record = sickle.GetRecord(identifier=identifier,
                              metadataPrefix="xoai")
    return record.get_dotted_data(record.record_map[address])


def get_map(identifier: str):
    sickle = Sickle("https://dspace.cuni.cz/oai/nusl")
    sickle.class_mapping['GetRecord'] = XOAIRecord
    record = sickle.GetRecord(identifier=identifier,
                              metadataPrefix="xoai")
    return record.record_map


if __name__ == "__main__":
    # pprint(get_map("oai:dspace.cuni.cz:20.500.11956/115773"))
    pprint(get_source("thesis.grade", "oai:dspace.cuni.cz:20.500.11956/115864"))
