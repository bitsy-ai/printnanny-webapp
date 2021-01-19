
# Request URL: https://help.print-nanny.com/ghost/api/v3/admin/members/?include=labels%2Cemail_recipients
# Request Method: POST

# query params
# include=labels%2Cemail_recipients

# {"members":[{"name":"Leigh Johnson","email":"leigh@bitsy.ai","note":"","subscribed":true,"comped":false,"email_count":0,"email_opened_count":0,"email_open_rate":null,"labels":[]}]}

import requests # pip install requests
import jwt	# pip install pyjwt
from datetime import datetime as date
from celery import group, chord, shared_task
from django.contrib.auth import get_user_model


User = get_user_model()

# Admin API key goes here
key = 'YOUR_ADMIN_API_KEY'

# Split the key into ID and SECRET
id, secret = key.split(':')

# Prepare header and payload
iat = int(date.now().timestamp())

header = {'alg': 'HS256', 'typ': 'JWT', 'kid': id}
payload = {
    'iat': iat,
    'exp': iat + 5 * 60,
    'aud': '/v3/admin/'
}

# Create the token (including decoding secret)
token = jwt.encode(payload, bytes.fromhex(secret), algorithm='HS256', headers=header)

# Make an authenticated request to create a post
url = 'http://localhost:2368/ghost/api/v3/admin/members/'
headers = {'Authorization': 'Ghost {}'.format(token.decode())}
body = {'posts': [{'title': 'Hello World'}]}
r = requests.post(url, json=body, headers=headers)

print(r)

