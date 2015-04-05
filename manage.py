import os
from flask.ext.script import Manager
from ctfscore import app, db, models
from flask.ext.migrate import Migrate, MigrateCommand

"""
This script replaces any run.py you find online.
It makes it easier to handle managing the application

ex. python manage.py runserver -h 0.0.0.0:80
"""

manager = Manager(app)

app.config.from_object('config.BaseConfiguration')

migrate = Migrate(app,db)
manager.add_command('db', MigrateCommand)


@manager.shell
def make_shell_context():
    '''Drops into shell with context of app, allows for database manipulation'''
    return dict(app=app, db=db, models=models)


@manager.command
def createdb():
    '''Runs the db init, db migrate, db upgrade commands automatically'''
    os.system('python manage.py db init')
    os.system('python manage.py db migrate')
    os.system('python manage.py db upgrade')


@manager.command
def test():
    '''Runs the tests.'''
    command = 'nosetests --verbosity=2 --nocapture'
    os.system(command)


@manager.command
def clean():
    '''Cleans the codebase'''
    commands = ["find . -name '*.pyc' -exec rm -f {} \;", "find . -name '*.pyo' -exec rm -f {} \;",
                "find . -name '*~' -exec rm -f {} \;", "find . -name '__pycache__' -exec rmdir {} \;",
                "rm -f app.db", "rm -rf migrations"]
    for command in commands:
        print "Running " + command
        os.system(command)


if __name__ == "__main__":
    manager.run()
