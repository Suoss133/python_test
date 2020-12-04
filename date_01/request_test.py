import requests, json, re
import inspect as url

# request = requests.get('http://47.100.18.242:9000/api/hotpoint',params={'key':1})
# result = request.json()
# print(result)
# print(result['status'])
# print(request.status_code)
# print(result['status'] == 'success')

request = requests.get('https://movie.douban.com/top250', headers={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
})
text_str = request.text

patter = re.compile('<span class="title">([\u4e00-\u9fa5].*)</span>')
name = patter.findall(text_str)

print(name)
