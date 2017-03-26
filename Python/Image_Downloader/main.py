import random
import urllib.request

def download_web_image(url):
    name = random.randrange(1, 1000)
    full_name = str(name) + '.jpg'
    urllib.request.urlretrieve(url, full_name)

download_web_image('http://orig09.deviantart.net/5b72/f/2016/103/8/f/ajin_by_bakaroringu-d9ytgji.jpg')