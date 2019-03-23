from subprocess import call
import common
from _globals import apps

def configure():
    if False == common.is_cmd_installed("npm"):
        common.msg("System","npm is not installed","warn")
        return False

    common.msg("Perform ","npm config")
    proxy=apps['npm']

    if True== proxy['use_proxy']:
        call(["npm","config","set","proxy"      ,"{0}".format(proxy['http_proxy_target'])])
        call(["npm","config","set","https-proxy","{0}".format(proxy['https_proxy_target'])])
    else :
        call(["npm","config","rm","proxy"])
        call(["npm","config","rm","https-proxy"])
    # TODO or persistent file
    #~/.npmrc file:
    #proxy=http://username:password@proxy:port
    #https-proxy=http://username:password@proxy:port
    #https_proxy=http://username:password@proxy:port
