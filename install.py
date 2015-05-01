#!/usr/bin/env python3

import shutil
import os
import subprocess


def copy_files(path, filename):
    src = working_folder + filename
    dst = path + filename

    if not os.path.exists(path):
        os.mkdir(path)

    shutil.copy(src, dst)


working_folder = os.path.dirname(__file__) + os.sep
if working_folder == '.':
    working_folder = ''

print(working_folder)
user_folder = os.path.expanduser('~')
local_bin_folder = user_folder + os.sep + '.local/bin/'
local_contractor_folder = user_folder + os.sep + '.local/share/contractor/'

try:
    copy_files(local_bin_folder, 'subtitledownloader.py')
    copy_files(local_contractor_folder, 'subtitledownloader.contract')
    subprocess.call(['notify-send', 'SubtitleDownloader', 'Installation OK!'])
except Exception as e:
    subprocess.call(['notify-send', '-i', 'dialog-error', str(e)])
