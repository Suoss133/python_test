import requests,json
import inspect as url



request = requests.get('http://47.100.18.242:9000/api/hotpoint',params={'key':1})
result = request.json()
print(result)
print(result['status'])
print(request.status_code)
print(result['status'] == 'success')