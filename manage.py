from flask_script import Manager
from flask_migrate import MigrateCommand
from myapp import create_app

app = create_app('debug')

manage=Manager(app)
manage.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manage.run()
