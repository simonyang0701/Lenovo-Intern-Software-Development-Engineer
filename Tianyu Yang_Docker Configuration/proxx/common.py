import os
from subprocess import call
from _globals import apps

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def msg(title,data,type='ok'):
    title_color=bcolors.OKGREEN
    if type == 'ok':
        title_color=bcolors.OKGREEN
    if type == 'warn':
        title_color=bcolors.WARNING
    if type == 'fail':
        title_color=bcolors.FAIL
    if type == 'underline':
        title_color=bcolors.UNDERLINE
        
    print ("{2}***[{3}{0}{2}]***{4} {1}".format(title,data,bcolors.OKBLUE,title_color,bcolors.ENDC))

def is_cmd_installed(cmd):
    res=call(['which',cmd])
    if 0==res:
        return True
    return False


def create_file(path,filename,data):
    file_path=path+filename
    with open(file_path, 'wb') as temp_file:
        temp_file.write(data)


def create_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)


def am_i_behind_a_proxy():
    return False


def is_this_a_docker():
    exit_code=call(['/usr/bin/grep','docker','/proc/self/cgroup','-qa'])
    if 0 == exit_code:
        return True
    return False
    

def print_config(config):
    print ("[{}]".format(config))
    for key in apps[config]:
        if None != apps[config][key]:
            print ("{0} = {1}".format(key,apps[config][key]))