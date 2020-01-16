from oarepo_nusl_rules.register import RuleRegistry


def rule(func):
    RuleRegistry.Instance().register(func)

    return func
