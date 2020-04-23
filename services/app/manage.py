"""TODO"""
from flask.cli import FlaskGroup
from werkzeug.security import generate_password_hash
from project import db, create_app
from project.models import User

cli = FlaskGroup()


@cli.command("create_db")
def create_db():
    """Create the DB tables"""
    db.drop_all()
    db.create_all(app=create_app())
    db.session.commit()
    print("*Tables Done*")


@cli.command("seed_db")
def seed_db():
    """This will insert dummy data for testing"""
    db.session.add(
        User(
            email="test@mail.com",
            name="test",
            password=generate_password_hash("test", method="sha256"),
        )
    )
    db.session.commit()
    print("User added as test")


##fds,fmdmnfdnjfdfndnfdd


if __name__ == "__main__":
    cli()
