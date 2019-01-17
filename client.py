import http.client

conn = http.client.HTTPConnection('dynupdate.no-ip.com')

url = '/nic/update?hostname=evilbaal.hopto.org&myip=186.61.97.220'

conn.request(
        'GET',
        url, 
        headers = {'Authorization': 'Basic ZXZpbGJhYWw6bm9pcC5jb20K',
                   'User-Agent': 'bolichep noip-client/0.1 bolichep@gmail.com'})

resp = conn.getresponse()

if resp.status == 200 and resp.reason == 'OK':
    data = resp.read()
    return_code, setted_ip = data.split()
    print(return_code, setted_ip)

