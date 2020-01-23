from oarepo_oai_parsers.register import Parser


class Mapper:
    """
    Docs
    """

    def __init__(self, parser: Parser):
        """

        """
        self.nusl_dict = {}
        self.parser = parser
        self.source_metadata = {}
