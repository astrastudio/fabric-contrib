# coding=utf-8
from fabric.api import run


def django_collectstatic(python, manage):
    run('yes yes | {} {} collectstatic'.format(python, manage))


def django_syncdb(python, manage):
    run('{} {} syncdb'.format(python, manage))


def django_migrate(python, manage):
    cmd = '{} {} migrate --noinput -v0 --merge --ignore-ghost-migrations'\
        .format(python, manage)
    run(cmd)
