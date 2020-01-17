from oarepo_nusl_rules import rule_registry
from oarepo_nusl_rules.register import RuleRegistry


def test_register_load():
    instance1 = RuleRegistry.Instance()
    RuleRegistry.Instance().load()
    instance2 = RuleRegistry.Instance()
    assert len(RuleRegistry.Instance().rules) > 0
    assert instance1 is instance2


def test_register_instance():
    instance1 = rule_registry
    instance2 = RuleRegistry.Instance()
    assert instance1 is instance2
