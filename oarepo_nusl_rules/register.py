import pkg_resources


class RuleRegistry(object):

    def __new__(cls):
        """
        Singleton design pattern (https://gist.github.com/lalzada/3938daf1470a3b7ed7d167976a329638)
        """
        if not hasattr(cls, 'instance') or not cls.instance:
            cls.instance = super().__new__(cls)

        return cls.instance

    def __init__(self, entry_point_group="oarepo_nusl_rules.rules"):
        self.loaded = False
        self.rules = {}
        self.entry_point_group = entry_point_group

    def load(self):
        if not self.loaded:
            for entry_point in pkg_resources.iter_entry_points(self.entry_point_group):
                ep = entry_point.load()
                pass

    def register(self, func):
        self.rules[func.__name__] = func
        print(RuleRegistry.instance.rules)


RuleRegistry()

if __name__ == "__main__":
    RuleRegistry.instance.load()
    print(RuleRegistry.instance.rules)
