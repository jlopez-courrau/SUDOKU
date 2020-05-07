"""SUDOKU WEB application"""
from flask.cli import FlaskGroup
from werkzeug.security import generate_password_hash
from project import db, create_app
from project.models import User

cli = FlaskGroup(create_app())


@cli.command("create_db")
def create_db():
    """Create the DB tables"""
    db.drop_all()
    db.create_all(app=create_app())
    db.session.commit()


@cli.command("seed_db")
def seed_db():
    """This will insert data for testing purpose"""
    db.session.add(
        User(
            email="test@mail.com",
            name="test",
            password=generate_password_hash("test", method="sha256"),
        )
    )
    print("User added as test")
    db.session.commit()


if __name__ == "__main__":
    cli()
