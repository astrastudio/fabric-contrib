# coding=utf-8
from fabric.api import env, run


COMMAND_COLLECTSTATIC = 'collectstatic'
COMMAND_SYNCDB = 'syncdb'
COMMAND_MIGRATE = 'migrate'

_default_command = '{python} {manage} {command}'
_commands_list = {
    COMMAND_COLLECTSTATIC: 'yes yes | {python} {manage} {command}',
    COMMAND_MIGRATE: '{python} {manage} {command} --noinput -v0 --merge '
                     '--ignore-ghost-migrations',
}


def django_commands():
    for command in env.django_commands:
        _django_command(command)


def _django_command(command):
    command_to_run = _commands_list.get(command, _default_command)
    command_to_run = command_to_run.format(
        python=env.server_python,
        manage=env.server_manage,
        command=command
    )

    run(command_to_run)
