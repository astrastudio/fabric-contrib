# coding=utf-8
import os
from fabric.api import cd, run
from fabric.contrib.files import exists


def virtualenv_create(path):
    if exists(path):
        return

    path, name = os.path.split(path)
    with cd(path):
        run('virtualenv {}'.format(name))


def virtualenv_copy(original, new):
    if not exists(original):
        raise ValueError('Original virtualenv not exists')

    if exists(new):
        raise ValueError('New virtualenv already exists')

    run('virtualenv-clone {} {}'.format(original, new))


def pip_install(pyenv_path, requirements_path):
    if not exists(pyenv_path):
        raise ValueError('Virtualenv not exists')

    if not exists(requirements_path):
        raise ValueError('Requirements not exists')

    pip_path = '{}/bin/pip'.format(pyenv_path)

    cmd = '{pip} install -r {filepath}'.format(
        pip=pip_path,
        filepath=requirements_path
    )

    run(cmd)
