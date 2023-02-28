import click
from flask import Blueprint


bp = Blueprint('tests', __name__, cli_group='tests')


@bp.cli.command('load_data')
def load_data():
    """Load basic data in csv files in the database with pandas library."""
    click.echo("Oh Oh End In Praise !")