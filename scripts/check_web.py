import requests as r

# Add your websites or url here:
urls = [
    'https://eosargentina.io',
    'https://eldolarbtc.com', # cloudflare
    'https://criptotendencias.com',
    'https://hashmasksnames.com' # cloudflare
]

def check(url_list):
    for url in urls:
        try:
            result = r.get(url)
            print('URL: {}, Status: OK'.format(url), result)
        except Exception as e:
            print(url, e)

check(urls)

# same thing but shorter, this for loop may be handy in future.
#responses = [r.get(url) for url in urls]
#print(responses)
