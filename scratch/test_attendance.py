import requests
url = 'http://127.0.0.1:8000/Attendance/Add'
payload = {'employee_id': 'test_emp', 'date': '2023-01-01', 'status': 'present'}
resp = requests.post(url, json=payload)
print('Status code:', resp.status_code)
print('Response:', resp.text)
