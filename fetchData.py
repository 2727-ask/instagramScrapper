import json
from datetime import datetime

import requests
from fastapi import FastAPI

app = FastAPI()


@app.get('/fetchReel/{id}')
def fetchReel(id):
    link = 'https://www.instagram.com/accounts/login/'
    login_url = 'https://www.instagram.com/accounts/login/ajax/'

    time = int(datetime.now().timestamp())
    response = requests.get(link)
    csrf = response.cookies['csrftoken']

    s = requests.Session()
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
    res = s.post(login_url,data=payload,headers=login_header)
    print(res.content)
    return("Hello World")


