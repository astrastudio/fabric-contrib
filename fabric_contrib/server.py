# coding=utf-8
import os
from fabric.api import cd, run, local, put


def service_restart(service_name):
    run('sudo /usr/sbin/service {} restart'.format(service_name))


def service_stop(service_name):
    run('sudo /usr/sbin/service {} stop'.format(service_name))


def service_start(service_name):
    run('sudo /usr/sbin/service {} start'.format(service_name))


def upload_to_server(local_dir, remote_dir):
    remote_path, remote_name = os.path.split(remote_dir)
    tar_file = "%s.tar.gz" % remote_name

    target_tar = os.path.join('/', 'tmp', tar_file)
    tar_path = os.path.join(local_dir, tar_file)

    items = ' '.join(os.listdir(local_dir))
    local("tar -czf %s -C %s %s" % (tar_path, local_dir, items))
    put(tar_path, target_tar)

    with cd(remote_path):
        try:
            run("mkdir -p {}".format(remote_name))
            run("tar -xzf {} -C {}".format(target_tar, remote_name))
        finally:
            run("rm -f %s" % target_tar)