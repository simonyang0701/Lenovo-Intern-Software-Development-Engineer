import argparse 
import configparser
import os
from subprocess import call

from _globals import apps
import configuration
import common
import app_docker
import app_git   
import app_gradel
import app_maven 
import app_npm   
import app_shell 
import app_yarn  
 

if __name__ == "__main__":
    parser = argparse.ArgumentParser("proxx", usage='%(prog)s [options]'
                    ,description=
                    """proxy configurator for applications
                       https* variables are optional, and willl be set to the http counterparts if not set
                    """, epilog="And that's how you'd proxx")

    # actions
    parser.add_argument('-l'      ,'--list'           , help= 'show available proxy applications'   , action='store_true')
    parser.add_argument('-c'      ,'--config'         , help= 'show config'                         , action='store_true')
    parser.add_argument('-r'      ,'--remove'         , help= 'remove all proxy configurations'     , nargs='?', default=False)
    
    # config parameters
    parser.add_argument('-uri'    ,'--proxy'          , help= 'the endpoint http proxy')
    parser.add_argument('-prt'    ,'--port'           , help= 'the endpoint http proxy')
    parser.add_argument('-usr'    ,'--username'       , help= 'the http user for the http proxy')
    parser.add_argument('-pwd'    ,'--password'       , help= 'the password for the http proxy')
    parser.add_argument('-suri'   ,'--https-proxy'    , help= 'the endpoint https proxy')
    parser.add_argument('-sprt'   ,'--https-port'     , help= 'the endpoint https proxy')
    parser.add_argument('-susr'   ,'--https-username' , help= 'the http user for the https proxy')
    parser.add_argument('-spwd'   ,'--https-password' , help= 'the password for the https proxy')
    parser.add_argument('-np'     ,'--no-proxy'       , help= 'the password for the https proxy')
 
    # app configs
    parser.add_argument('-a'      ,'--all'            , help= 'apply to "all applications"'         , action='store_true')
    for app in apps:
        parser.add_argument('--{0}'.format(app) , help= 'apply to {0}'.format(app) , action='store_true')
 

    args = parser.parse_args()
    config_changed=False
    use_proxy=True
    is_docker=common.is_this_a_docker()
    common.msg("Status","This is not a Docker")
    configuration.load_config()
    
    #print (apps)
    if True== args.list:
        for app in apps:
            common.msg("Applications",app)


    #TODO split proxy url to ease use
    # set proxy vars
    proxy=configuration.set_proxy(  http_proxy =args.proxy      ,http_port =args.port      ,http_username =args.username      ,http_password =args.password,
                                    https_proxy=args.https_proxy,https_port=args.https_port,https_username=args.https_username,https_password=args.https_password,
                                    noproxy=args.no_proxy,dont_set_use=False)
    updates=[]
    for app in apps:
        if True == args.all or args[app]==True:
            common.msg('Status','{0} updated'.format(app))
            apps[app]=proxy
            config_changed=True

        if args.remove==app or args.remove==None:
            common.msg('Status','{0} proxy is off'.format(app))
            apps[app]['use_proxy']=False
            config_changed=True


    if True == config_changed:
        common.msg('Status','Saving')
        configuration.save_config()

    if True == args.config:
        for app in apps:
            common.print_config(app)


    if False == is_docker:
        # cant configure a docker inside a docker
        if True == args.all or True == args.docker:
            app_docker.configure()
    
    if True == args.all or True == args.git:
        app_git.configure()
    if True == args.all or True == args.npm:
        app_npm.configure()
    if True == args.all or True == args.yarn:
        app_yarn.configure()
    #if True == args.all or True == args.shell:
    #    configure_shell()
