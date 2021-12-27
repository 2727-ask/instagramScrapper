from fastapi import FastAPI
import requests
import json

app = FastAPI()

@app.get('/fetchReel/{id}')

def fetchReel(id):

    try:
        from urllib.parse import urlparse
    except ImportError:
        import urlparse

    BASE_URL = 'https://www.instagram.com/'
    CHROME_WIN_UA = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'

    session = requests.Session()
    session.headers = {'user-agent': CHROME_WIN_UA, 'Referer': BASE_URL}
    session.cookies.set('ig_pr', '1')
    req = session.get(BASE_URL)
    session.headers.update({'X-CSRFToken': req.cookies['csrftoken']})

    url = f"https://www.instagram.com/reel/{id}/?__a=1"
    response = session.get(url, cookies="", headers={'Host': urlparse(url).hostname}, stream=False, timeout=90)
    return(f"{response}")
