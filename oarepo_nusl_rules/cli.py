import click
from flask import cli
from invenio_db import db

from invenio_oarepo_oai_pmh_harvester.models import OAIRule
from oarepo_nusl_rules.register import rule_registry


@click.group()
def oai():
    """OAI harvester commands"""


@oai.group()
def register():
    pass


@register.command('rules')
@cli.with_appcontext
def rules():
    rule_registry.load()
    rules_ = rule_registry.rules
    for k, v in rules_.items():
        code = k
        description = v.__doc__
        existed_rule = OAIRule.query.filter_by(code=code).one_or_none()
        if existed_rule is None:
            rule = OAIRule(code=code, description=description)
            print("Rule", rule, db.engine)
            db.session.add(rule)
            db.session.commit()


