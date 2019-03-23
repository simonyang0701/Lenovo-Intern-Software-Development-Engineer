from subprocess import call
import common
from _globals import apps

def configure():
    if False == common.is_cmd_installed("git"):
        common.msg("System","git is not installed","warn")
        return False

    common.msg("Perform ","git config")
    proxy=apps['git']


    print proxy['use_proxy']
    
    if True == proxy['use_proxy']:
        print "Setting"
        call(["/usr/bin/git","config","--global","http.proxy" ,"{0}".format(proxy['http_proxy_target']) ])
        call(["/usr/bin/git","config","--global","https.proxy","{0}".format(proxy['https_proxy_target']) ])
    else:
        print ("Unsetting")
        call(["/usr/bin/git","config","--global","--unset","http.proxy"])
        call(["/usr/bin/git","config","--global","--unset","https.proxy"])
    # TODO persistent config
    #~/.gitconfig file:
    #[http]
    #    proxy = http://username:password@proxy:port
    #[https]
    #    proxy = http://username:password@proxy:port
