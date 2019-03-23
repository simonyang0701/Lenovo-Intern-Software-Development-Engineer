import os
from subprocess import call
import common
from _globals import apps


# TODO will; never work
def configure():
    common.msg("Perform ","shell config")
    proxy=apps['shell']

    if True== proxy['use_proxy']:
        #call(["export","HTTP_PROXY={0} ".format(proxy['http_proxy_target'])])
        #call(["export","HTTPS_PROXY={0}".format(proxy['https_proxy_target'])])
        os.environ["HTTP_PROXY"] = "{0}".format(proxy['http_proxy_target'])
        os.environ["HTTPS_PROXY"] = "{0}".format(proxy['https_proxy_target'])

    else:
        call(["unset","HTTP_PROXY"])
        call(["unset","HTTPS_PROXY"])
    


