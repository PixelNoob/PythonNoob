import subprocess
from subprocess import Popen

# ping a list of different hosts
urls = [
    'eosargentina.io',
    'eldolarbtc.com',
    'criptotendencias.com',
    'hashmasksnames.com',
    'senseinode.com'
]

def ping_hosts(hosts):
    for url in hosts:
        ping = subprocess.Popen(['ping', '-c', '1', url], stdout=subprocess.PIPE, stderr = subprocess.PIPE, text=True)
        out, error = ping.communicate('')
        #if out:
        #    print(out)
        #else:
        #    print(url, error)
        # compare speed
        start= out.find('time=')
        finish = out.find("ms",start)
        speed= out[start:finish+2]
        print('{} Latency:'.format(url), speed)

ping_hosts(urls)

# check only one website
host = "eldolarbtc.com"

def ping(url):
    ping = subprocess.Popen(['ping', '-c', '1', host], stdout=subprocess.PIPE, stderr = subprocess.PIPE, text=True)
    out, error = ping.communicate('')
    if out:
        return(out)
    else:
        return(url, error)

#res = ping(host)
#print(res)

# get latency
def latency(out):
    start= out.find('time=')
    finish = out.find("ms",start)
    speed= out[start:finish+2]
    return('Latency', speed)

#latency = latency(res)
#print(latency)
