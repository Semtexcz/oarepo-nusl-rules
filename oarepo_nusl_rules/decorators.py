from oarepo_nusl_rules.register import RuleRegistry


def rule(func):
    RuleRegistry.instance.register(func)

    return func
