import sqlite3

import click
import datetime
from flask import current_app, g


# Register converter to sqlite3
def convert_date(val):
    """Convert ISO 8601 date to datetime.date object."""
    return datetime.date.fromisoformat(val.decode())

sqlite3.register_converter("date", convert_date)


def init_app(app):
    '''Set some default options about db to app'''

    # close db connection when appcontext ends
    app.teardown_appcontext(close_db) 

    # register new command to create DB schema
    app.cli.add_command(init_db_command)


def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


def get_db():
    '''Returns current db connection. Create new if not exists'''
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    '''Close db'''
    db = g.pop('db', None)

    if db is not None:
        db.close()
