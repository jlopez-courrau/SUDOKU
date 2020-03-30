"""
TODO: Add docstring
File: manage.py
Author: yourname
Description:
"""
from flask.cli import FlaskGroup
from project import app #, db, add db models here

cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    # db.drop_all()
    # db.create_all()
    # db.session.commit()
    print("TODO")


@cli.command("seed_db")
def seed_db():
    # db.session.add(#something)
    # db.session.commit()
    pass


if __name__ == "__main__":
    cli()
