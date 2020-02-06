from __future__ import absolute_import, print_function

import os
import shutil
import tempfile

import pytest
from flask import Flask
from invenio_app.factory import create_api
from invenio_db import InvenioDB
from invenio_db import db as db_
from invenio_jsonschemas import InvenioJSONSchemas
from invenio_records import InvenioRecords
from sqlalchemy_utils import create_database, database_exists

from flask_taxonomies import FlaskTaxonomies
from flask_taxonomies.views import blueprint as taxonomies_blueprint


@pytest.fixture(scope='module')
def create_app():
    """Create test app."""
    return create_api


@pytest.yield_fixture()
def app():
    instance_path = tempfile.mkdtemp()
    _app = Flask('testapp', instance_path=instance_path)

    _app.config.update(
        JSONSCHEMAS_HOST="nusl.cz",
        SQLALCHEMY_TRACK_MODIFICATIONS=True,
        SQLALCHEMY_DATABASE_URI=os.environ.get(
            'SQLALCHEMY_DATABASE_URI',
            'sqlite:////home/semtex/Projekty/nusl/invenio-oarepo-oai-pmh-harvester/venv/lib'
            '/python3.7/site-packages/invenio/db.sqlite3'),
        SERVER_NAME='localhost',
    )
    InvenioJSONSchemas(_app)
    InvenioRecords(_app)
    InvenioDB(_app)
    FlaskTaxonomies(_app)
    with _app.app_context():
        _app.register_blueprint(taxonomies_blueprint)
        yield _app

    shutil.rmtree(instance_path)


@pytest.yield_fixture()
def db(app):
    """Database fixture."""
    if not database_exists(str(db_.engine.url)):
        create_database(str(db_.engine.url))
    yield db_
