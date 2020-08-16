"""
                                tests.conftest
                                ~~~~~~~~~~~~~~

    In this module we can find all configurations and fixtures needed to run
    all the necessary tests that help maintain this application.

    :copyright: 2020 TFreire
    :licence: [...]
"""

import pytest
from app import app
from app import mysql


@pytest.fixture
def cursor():
    """
        Fixture ensures connection for the purpose of testing the DB.
    """
    with app.app_context():
        cursor = mysql.connection.cursor()
        yield cursor
        mysql.connection.rollback()


@pytest.fixture
def tables():
    """
        Fixture provides sequence of table names to check whether or not they
        exist in the DB.
    """
    tables = (
        ("fundos",),
        ("orgaos",),
        ("chancelas",),
        ("periodicos",),
        ("periodicos_numeros",),
        ("partituras",)
    )
    return tables
