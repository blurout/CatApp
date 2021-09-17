import requests
from PIL import Image
from io import BytesIO


def get_cat_image():
    r = requests.get('https://api.thecatapi.com/v1/images/search', params={'x-api-key': get_api_key()})
    data = r.json()
    url = data[0]['url']
    response = requests.get(url)
    return BytesIO(response.content)


def get_api_key():
    f = open('key.config', 'r')
    key = f.read()
    f.close()
    return key


if __name__ == '__main__':
    for i in range(0, 3):
        img = Image.open(get_cat_image())
        img.show()