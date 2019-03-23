import os
import configparser
from subprocess import call
import common
from _globals import proxy_var
from _globals import apps



def load_config():
    config_file=os.path.expanduser('~/.proxx.ini')
    exists = os.path.isfile(config_file)
    if True != exists:
        return
    config = configparser.ConfigParser(allow_no_value=True)
    config.read(config_file)
    try:
        for key in apps:
            if  True == config.has_section(key):
                for sub_key in proxy_var:
                    if  True == config.has_option(key,sub_key):
                        #print (key,sub_key)
                        if 'use_proxy' == sub_key:
                            apps[key][sub_key]=config[key].getboolean(sub_key)
                        else:
                            apps[key][sub_key]=config[key][sub_key]
            set_targets(key)
    except Exception as ex:
        common.msg("Loading config Err:",ex,"fail")

def save_config():
    #return
    config_file=os.path.expanduser('~/.proxx.ini')

    config = configparser.ConfigParser(allow_no_value=True)
    try:
        header="""[defaults]
http_username      = sam         ; HTTP proxy credential (Not needed if setup in CNTLM)
http_password      = sampwd      ; HTTP proxy credential (Not needed if setup in CNTLM)
http_proxy         = localhost   ; HTTP proxy uri
http_port          = 3128        ; HTTP proxy port
https_username     = sam         ; * The same as above, but for HTTPS
https_password     = sampw       ; * If omitted, the http option is used
https_proxy        = localhost   ; *
https_port         = 3128        ; *
no_proxy           = website.com website2.com website 3.com   ; usually internal sites
use_proxy          = comments    ; enable or disable this proxy config


"""

        #print proxy_var
        for key in apps:
            config[key]={}
            remove_section=True
            for sub_key in apps[key]:
                if sub_key in proxy_var:
                    if None != apps[key][sub_key]:
                        value="{0}".format(apps[key][sub_key])
                        config[key][sub_key]=value
                        remove_section=False
            if True == remove_section:
                config.remove_section(key)

        config.remove_section('defaults')
        with open(config_file, 'w') as configfile:
            #configfile.write(header)
            config.write(configfile)
    except Exception as ex:
        common.msg("Saving config",ex,"fail")



def set_targets(config):
    http_proxy       =None
    http_port        =None
    http_username    =None
    http_password    =None
    https_proxy      =None
    https_port       =None
    https_username   =None
    https_password   =None
    no_proxy         =None

    if 'http_proxy'     in apps[config]:
        http_proxy    = apps[config]['http_proxy']
    if 'http_port'      in apps[config]:
        http_port     = apps[config]['http_port']
    if 'http_username'  in apps[config]:
        http_username = apps[config]['http_username']
    if 'http_password'  in apps[config]:
        http_password = apps[config]['http_password']
    if 'https_proxy'    in apps[config]:
        https_proxy   = apps[config]['https_proxy']
    if 'https_port'     in apps[config]:
        https_port    = apps[config]['https_port']
    if 'https_username' in apps[config]:
        https_username= apps[config]['https_username']
    if 'https_password' in apps[config]:
        https_password= apps[config]['https_password']
    if 'no_proxy'        in apps[config]:
        no_proxy      = apps[config]['no_proxy']

    
    apps[config]=set_proxy(http_proxy ,http_port ,http_username ,http_password,
                           https_proxy,https_port,https_username,https_password,no_proxy,dont_set_use=True)


def set_proxy(http_proxy ="127.0.0.1",http_port ="3128",http_username =None,http_password=None,
              https_proxy=None       ,https_port=None  ,https_username=None,https_password=None,noproxy=None,dont_set_use=False):
    """Configure individual proxy settings per application"""
    app_proxy={}
    app_proxy['no_proxy']=noproxy
    
    if http_proxy == None and https_proxy == None:
        app_proxy['use_proxy']=False
        

    if None == http_username:
        if http_proxy == None:
            app_proxy['http_proxy_target']=None
        else:
            app_proxy['http_proxy_target']="{0}:{1}".format(http_proxy,http_port)
        app_proxy['http_proxy']  =http_proxy
        app_proxy['http_port']   =http_port
        app_proxy['http_username']=http_username
        app_proxy['http_password']=http_password
    else:
        app_proxy['http_proxy_target']="{0}:{1}@{2}:{3}".format(http_username,http_password,http_proxy,http_port)
        app_proxy['http_proxy']   =http_proxy
        app_proxy['http_port']    =http_port
        app_proxy['http_username']=http_username
        app_proxy['http_password']=http_password


    # if no https is set.. duplicate parameters
    if None == https_proxy:
        app_proxy['https_proxy_target']=app_proxy['http_proxy_target']
        app_proxy['https_proxy']   =http_proxy
        app_proxy['https_port']    =http_port
        app_proxy['https_username']=http_username
        app_proxy['https_password']=http_password
    else:
        # if one is set, make target like http
        if None == https_username:
            app_proxy['https_proxy_target']="{0}:{1}".format(https_proxy,https_port)
            app_proxy['https_proxy']   =https_proxy
            app_proxy['https_port']    =https_port
        else:
            app_proxy['https_proxy_target']="{0}:{1}@{2}:{3}".format(https_username,https_password,https_proxy,https_port)
            app_proxy['https_proxy']   =https_proxy
            app_proxy['https_port']    =https_port
            app_proxy['https_username']=https_username
            app_proxy['https_password']=https_password
    if False == dont_set_use:
        app_proxy['use_proxy']=True
    return app_proxy
