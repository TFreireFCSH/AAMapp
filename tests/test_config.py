"""
                            tests.test_config
                            ~~~~~~~~~~~~~~~~~

    This module has all the tests that concern the configuration of the
    application.

    :copyright: 2020 TFreire
    :licence: [...]
"""


def test_connect_mysql(cursor):
    """
        Tests whether or not a connection to the DB can be established by
        trying to query a table.
    """
    cursor.execute("""SELECT fundos_id FROM fundos;""")
    data = cursor.fetchall()
    assert len(data) > 0


def test_schema_config(cursor):
    """
        Tests whether or not the selected schema is 'aam'.
    """
    cursor.execute("""SELECT DATABASE();""")
    data = cursor.fetchone()
    assert data[0] == "aam"


def test_schema_table(cursor, tables):
    """
        Ensures schema consistency by varifying that all tables are present.
    """
    cursor.execute("""SHOW TABLES;""")
    data = cursor.fetchall()
    for table in tables:
        assert table in data
