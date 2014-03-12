# coding=utf-8
from fabric.api import env, run


COMMAND_COLLECTSTATIC = 'collectstatic'
COMMAND_SYNCDB = 'syncdb'
COMMAND_MIGRATE = 'migrate'


def django_command(command):
    _command = {
        'default': '{python} {manage} {command}',

        COMMAND_COLLECTSTATIC: 'yes yes | {python} {manage} {command}',
        COMMAND_MIGRATE: '{python} {manage} {command} --noinput -v0 --merge '
                         '--ignore-ghost-migrations',
    }

    command = _command.get(command, command['default'])
    command.format(
        python=env.server_python,
        manage=env.server_manage,
        command=command
    )
    run(command)
