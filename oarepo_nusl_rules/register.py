"""
Docs
"""

import pkg_resources

ENTRY_POINT_GROUP = "oarepo_nusl_rules.rules"


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

    def __init__(self):
        self.loaded = False
        self.rules = {}
        self.entry_point_group = ENTRY_POINT_GROUP

    def load(self):
        if not self.loaded:
            for entry_point in pkg_resources.iter_entry_points(self.entry_point_group):
                entry_point.load()

    def register(self, func):
        self.rules[func.__name__] = func


rule_registry = RuleRegistry.Instance()
