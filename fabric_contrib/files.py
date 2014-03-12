# coding=utf-8
import os
import uuid
from contextlib import contextmanager
from fabric.api import local


@contextmanager
def save_original_file(file_path):
    tmp_file = os.path.join('/', 'tmp', unicode(uuid.uuid4()))
    lcp(file_path, tmp_file)
    yield
    lcp(tmp_file, file_path)


def lmkdir(directory, delete_if_exists=False):
    if os.path.exists(directory):
        if delete_if_exists:
            lrm(directory)
        else:
            message = 'Path "{}" exists.'.format(directory)
            raise ValueError(message)

    local('mkdir -p {}'.format(directory))


def lrm(unlink_path):
    local('rm -rf {}'.format(unlink_path))


def lcp(source_path, target_path):
    local('cp -R {} {}'.format(source_path, target_path))


def lclear(path, file_parent):
    local('find {} -name "{}" -exec rm -rf {{}} \;'.format(path, file_parent))
