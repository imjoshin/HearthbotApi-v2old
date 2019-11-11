import os
import unittest
import sys

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import blueprint
from app.main import create_app, db

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.register_blueprint(blueprint)
app.app_context().push()

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.command
def run():
    app.run(host='0.0.0.0', port=8081)


@manager.command
def test():
    """Runs the unit tests."""
    glob = os.environ['GLOB'] if os.environ.get('GLOB', None) else 'test*.py'
    tests = unittest.TestLoader().discover('app/test', pattern=glob)
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    return 0 if result.wasSuccessful() else 1


if __name__ == '__main__':
    manager.run()
