# coding=utf-8
import os
import uuid

from fabric.api import local

from fabric_contrib.files import lrm


def less_compilation(less_file, css_file):
    command = 'lessc {} >> {}'.format(less_file, css_file)
    local(command)


def compress_css(css_file):
    pass


def js_compilation(coffee_source_dir, eco_source_dir, vendor_source_dir,
                   vendor_files, js_file):
    tmp_coffee = '/tmp/{}'.format(uuid.uuid4())
    tmp_eco = '/tmp/{}'.format(uuid.uuid4())

    coffeescript_compilation(coffee_source_dir, tmp_coffee)
    eco_compilation(eco_source_dir, tmp_eco)

    vendor_files = [os.path.join(vendor_source_dir, x) for x in vendor_files]
    vendor_files.append(tmp_eco)
    vendor_files.append(tmp_coffee)

    files_concat(vendor_files, js_file)

    local('rm {}'.format(tmp_coffee))
    local('rm {}'.format(tmp_eco))


def coffeescript_concat(source_dir, coffee_file):
    dirs = [source_dir]
    for dir_name, dir_names, file_names in os.walk(source_dir):
        for sub_dir_name in dir_names:
            dirs.append(
                os.path.join(dir_name, sub_dir_name)
            )

    cmd = 'coffeescript-concat -I {} -o {}'.format(
        ' -I '.join(dirs), coffee_file
    )
    local(cmd)


def coffeescript_compilation(source_dir, coffee_file):
    tmp_file = '/tmp/{}'.format(uuid.uuid4())

    coffeescript_concat(source_dir, tmp_file)
    local('coffee -p --compile {} >> {}'.format(tmp_file, coffee_file))

    local('rm {}'.format(tmp_file))


def eco_compilation(source_dir, js_file):
    tmp_dir = '/tmp/{}'.format(uuid.uuid4())

    cmd = 'eco -i JST {} -o {}  >/dev/null 2>/dev/null'\
        .format(source_dir, tmp_dir)
    local(cmd)

    cmd = 'cat `find {} -type f -name "*.js" | ' \
          'awk \'{{ print $1" "}}\'| tr -d " "` >>{}'.format(tmp_dir, js_file)
    local(cmd)

    lrm(tmp_dir)


def files_concat(files, target_file):
    files = ' '.join(files)
    cmd = 'cat {} > {}'.format(files, target_file)
    local(cmd)
