import requests

payload = {
    'content': "MESSAGE"
}

header = {
    'authorization': 'Authorization'
}

r = requests.post('Request URL', data=payload, headers=header)
