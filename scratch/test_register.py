import requests

url = 'http://127.0.0.1:8000/User/register'
payload = {
    'username': 'testuser',
    'password': 'testpass',
    'role': 'employee'
}
response = requests.post(url, json=payload)
print('Status code:', response.status_code)
print('Response:', response.text)
