import requests
from utils.tokens import url_short

def short_url(url: str):
    responce = requests.post(
        url="https://clc.li/api/url/add",
        headers={
            'Authorization': f'{url_short}',
            'Content-Type': 'application/json'
            },
            json={
                'url': f'{url}'
            })
    short_url = responce.json()
    try:
        return short_url['shorturl']
    except:
        return short_url['message']
