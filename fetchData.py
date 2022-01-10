from datetime import datetime

import requests
from fastapi import FastAPI
import json

app = FastAPI()


class AuthSession:
    s = requests.Session()
    isLoggedIn = False
    def authenticate(self):
        link = 'https://www.instagram.com/accounts/login/'
        login_url = 'https://www.instagram.com/accounts/login/ajax/'

        time = int(datetime.now().timestamp())
        print(time)
        response = requests.get(link)
        csrf = response.cookies['csrftoken']
        print("CSRF TOKEN", csrf);
        payload = {
            'username': 'carrylinati',
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:Asdfghjkl@27',
            'queryParams': {},
            'optIntoOneTap': 'false'
        }
        login_header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
            "Referer": "https://www.instagram.com/accounts/login/",
            "x-csrftoken": "2T1msXxiNHNgpiVAANwtzrNB5IsrR1pT"
        }

        res = AuthSession.s.post(login_url, data=payload, headers=login_header)
        print(res.content)

        jsonData = json.loads(res.content)
        if (jsonData["authenticated"]):
            AuthSession.isLoggedIn = True
        else:
            AuthSession.isLoggedIn = False

    def fetchReel(self,id):
        res = AuthSession.s.get(f"https://www.instagram.com/p/{id}/?__a=1")
        return json.loads(res.content)


@app.get('/makeReq/{id}')
def makeReq(id):
    session = AuthSession()
    if(session.isLoggedIn == False):
        print("Authenticating")
        session.authenticate()
    else:
        print("Already Authenticated")
        return session.fetchReel(id)
