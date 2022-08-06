import os

from app import create_app
from flask_migrate import upgrade


app = create_app(os.getenv('FLASK_CONFIG') or 'default')


@app.cli.command()
def deploy():
    """Run deployment tasks"""
    # migrate database to latest revision
    upgrade()


if __name__ == '__main__':
    app.run()