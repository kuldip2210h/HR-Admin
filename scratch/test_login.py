import requests
url = 'http://127.0.0.1:8000/User/login'
payload = {'username': 'testuser', 'password': 'testpass'}
resp = requests.post(url, json=payload)
print('Status code:', resp.status_code)
print('Response:', resp.text)
