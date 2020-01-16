import pkg_resources


class Singleton:

    def __init__(self, cls):
        self._cls = cls

    def Instance(self):
        try:
            return self._instance
        except AttributeError:
            self._instance = self._cls()
            return self._instance

    def __call__(self):
        raise TypeError('Singletons must be accessed through `Instance()`.')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._cls)


@Singleton
class RuleRegistry(object):

    def __init__(self, entry_point_group="oarepo_nusl_rules.rules"):  # entry_point_group="oarepo_nusl_rules.rules"
        self.loaded = False
        self.rules = {}
        self.entry_point_group = entry_point_group

    def load(self):
        if not self.loaded:
            for entry_point in pkg_resources.iter_entry_points("oarepo_nusl_rules.rules"):
                ep = entry_point.load()
                pass

    def register(self, func):
        self.rules[func.__name__] = func
        print(RuleRegistry.Instance(), RuleRegistry.Instance().rules)


# RuleRegistry.Instance()

if __name__ == "__main__":
    c1 = RuleRegistry.Instance()
    RuleRegistry.Instance().load()
    print(RuleRegistry.Instance().rules, RuleRegistry.Instance())
    c2 = RuleRegistry.Instance()
    print(c1, c2, c1 is c2)
