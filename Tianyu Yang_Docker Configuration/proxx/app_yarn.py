from subprocess import call
from _globals import apps
import common

def configure():
    if False == common.is_cmd_installed("yarn"):
        common.msg("System","yarn is not installed","warn")
        return False

    common.msg("Perform ","yarn config")
    proxy=apps['yarn']

    if True== proxy['use_proxy']:
        call(["yarn","config","set","proxy"      ,"{0}".format(proxy['http_proxy_target'])])
        call(["yarn","config","set","https-proxy","{0}".format(proxy['https_proxy_target'])])
    else:
        call(["yarn","config","delete","proxy"])
        call(["yarn","config","delete","https-proxy"])


