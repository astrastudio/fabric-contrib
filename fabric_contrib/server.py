# coding=utf-8
import os
from fabric.api import cd, run, local, put
from fabric.contrib.files import upload_template


def service_restart(service_name):
    service_command(service_name, 'restart')


def service_stop(service_name):
    service_command(service_name, 'stop')


def service_start(service_name):
    service_command(service_name, 'start')


def service_command(service_name, command):
    run('sudo /usr/sbin/service {} {}'.format(service_name, command))


def upload_config(local_path, remote_path, params):
    file_name = os.path.basename(local_path)
    path = os.path.abspath(local_path)

    upload_template(
        file_name,
        remote_path,
        context=params,
        template_dir=path,
        use_jinja=True,
        use_sudo=False,
        backup=False
    )


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
