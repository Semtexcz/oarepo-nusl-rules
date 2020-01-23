from oarepo_nusl_rules.mapper import Mapper


class XOAIMapper(Mapper):
    """
    Docs
    """

    def xml_dict_to_nusl_dict(self, address=""):
        if address == "":
            self.source_metadata = self.parser.xml_to_dict["record"]["metadata"]["metadata"]
        # TODO: dodělat tabulku s mapováním

