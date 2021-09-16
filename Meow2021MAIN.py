import requests
f = open('key.config','r')
key = f.read()
f.close()

for i in range(1,100):
    r = requests.get('https://api.thecatapi.com/v1/images/search', params={'x-api-key': key})
    data = r.json()
    print(data[0]['url'])