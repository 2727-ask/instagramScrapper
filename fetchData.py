from fastapi import FastAPI
import requests
from datetime import datetime
import requests
import json

app = FastAPI()

@app.get('/fetchReel/{id}')

def fetchReel(id):
    link = 'https://www.instagram.com/accounts/login/'
    login_url = 'https://www.instagram.com/accounts/login/ajax/'

    time = int(datetime.now().timestamp())
    response = requests.get(link)
    csrf = response.cookies['csrftoken']

    payload = {
        'username': 'ashutoshkumbhar27',
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:Asdfghjkl@27',
        'queryParams': {},
        'optIntoOneTap': 'false'
    }

    login_header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": "https://www.instagram.com/accounts/login/",
        "x-csrftoken": csrf
    }

    login_response = requests.post(login_url, data=payload, headers=login_header)
    json_data = json.loads(login_response.text)

    if json_data["authenticated"]:

        print("login successful")
        cookies = login_response.cookies
        cookie_jar = cookies.get_dict()
        csrf_token = cookie_jar['csrftoken']
        print("csrf_token: ", csrf_token)
        session_id = cookie_jar['sessionid']
        print("session_id: ", session_id)

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

        return (response.content)


    else:
        print("login failed ", login_response.text)

