from fastapi import FastAPI
import requests
from datetime import datetime
import requests
import json

app = FastAPI()

isLoggedIn = False
s = requests.Session()


def authenticateSesssion():
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

    res = s.post(login_url, data=payload, headers=login_header)
    print(res.content)

    jsonData = json.loads(res.content)
    if (jsonData["authenticated"]):
        isLoggedIn = jsonData["authenticated"]
        return isLoggedIn
    else:
        return False



@app.get('/makeReq/{id}')
def makeReq(id):
    global isLoggedIn
    if(isLoggedIn == False):
        isLoggedIn = authenticateSesssion()
        return {
            'status':'again'
        }
    else:
        print("Authenticated")
        data = s.get(f"https://www.instagram.com/p/{id}/?__a=1")
        print("Data", data.content)
        return json.loads(data.content)


