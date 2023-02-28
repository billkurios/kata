import click
import pandas as pd
from flask import Blueprint

from ..properties.models.manager import Manager
from ..properties.models.property import Property
from ..db import db


bp = Blueprint('tests', __name__, cli_group='tests')


def genManagers(managersDF):
    """Generateur d'objets Manager à partir du dataframe
    issu de la lecture du fichier csv"""
    for value in managersDF.values:
        managerArgs = {}
        for i in range(len(value)):
            managerArgs[managersDF.columns[i]] = value[i]
        yield Manager(**managerArgs)

def genProperties(propertiesDF):
    """Generateur d'objets Property à partir du dataframe
    issu de la lecture du fichier csv"""
    for value in propertiesDF.values:
        propertyArgs = {}
        for i in range(len(value)):
            propertyArgs[propertiesDF.columns[i]] = value[i]
        yield Property(**propertyArgs)


@bp.cli.command('load_data')
def load_data():
    """Load basic data in csv files in the database with pandas library."""
    click.echo("Step 1: Import managers data")
    managerObjects = genManagers(pd.read_csv(r'./data/managers.csv'))
    for manager in managerObjects:
        db.session.add(manager)
    click.echo("Step 1 doned !!!")
    click.echo("Step 2: Import properties data")
    propertyObjects = genProperties(pd.read_csv(r'./data/properties.csv'))
    for property in propertyObjects:
        db.session.add(property)
    db.session.commit()
    click.echo("Step 2 doned !!!")