from  subprocess import call
import common
from _globals import apps

def configure():
    if False == common.is_cmd_installed("docker"):
        common.msg("System","docker is not installed","warn")
        return False
    common.msg("Perform ","docker config")
    proxy_dir        = '/etc/systemd/system/docker.service.d/'
    http_proxy_file  = 'http-proxy.conf'
    https_proxy_file = 'https-proxy.conf'

    proxy=apps['docker']
    if True== proxy['use_proxy']:
        comment=""
    else:
        comment="#"
    
    # Data
    http_proxy_content="""[Service]
    {1}Environment="HTTP_PROXY={0}"
    """.format(proxy['http_proxy_target'],comment)

    https_proxy_content="""[Service]
    {1}Environment="HTTPS_PROXY={0}"
    """.format(proxy['https_proxy_target'],comment)

    # action 
    common.create_dir(proxy_dir)
    common.create_file(proxy_dir,http_proxy_file ,http_proxy_content)
    common.create_file(proxy_dir,https_proxy_file,https_proxy_content)
    call(["service","docker","restart"])
    call(["systemctl","daemon-reload"])


  

