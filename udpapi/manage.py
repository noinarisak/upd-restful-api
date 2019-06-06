import click
from flask.cli import FlaskGroup

from udpapi.app import create_app

app = create_app()

def create_udpapi(info):
    return create_app(cli=True)


@click.group(cls=FlaskGroup, create_app=create_udpapi)
def cli():
    """Main entry point"""


@cli.command("init")
def init():
    """Init application, create database tables
    and create a new user named admin with password admin
    """
    from udpapi.extensions import db
    from udpapi.models import User
    click.echo("drop database")
    db.drop_all()
    click.echo("create database")
    db.create_all()
    click.echo("done")

    click.echo("create user")
    user = User(
        username='admin',
        email='admin@mail.com',
        password='admin',
        active=True
    )
    db.session.add(user)
    db.session.commit()
    click.echo("created user admin")


@cli.command("drop_db")
def drop_db():
    """Drops the db tables."""
    click.echo("drop database")
    db.drop_all()


if __name__ == "__main__":
    cli()

    import os
    if os.environ.get('PORT') is not None:
        app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT'))
    else:
        app.run(debug=True, host='0.0.0.0')
