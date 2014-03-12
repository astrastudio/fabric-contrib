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


def lmkdir(directory):
    local('mkdir -p {}'.format(directory))


def lrm(unlink_path):
    local('rm -rf {}'.format(unlink_path))


def lcp(source_path, target_path):
    local('cp -R {} {}'.format(source_path, target_path))


def lclear(path, file_parent):
    local('find {} -name "{}" -exec rm -rf {{}} \;'.format(path, file_parent))
