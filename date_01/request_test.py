import requests
import json
import re
import inspect as url


# request = requests.get('http://47.100.18.242:9000/api/hotpoint',params={'key':1})
# result = request.json()
# print(result)
# print(result['status'])
# print(request.status_code)
# print(result['status'] == 'success')


# 网络爬虫案例
# request = requests.get('https://movie.douban.com/top250', headers={
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
# })
# text_str = request.text
#
# patter = re.compile('<span class="title">([\u4e00-\u9fa5].*)</span>')
# name = patter.findall(text_str)
#
# print(name)

# 将request返回的内容写入文件
<<<<<<< HEAD
def set_request_context(method, url, **kwargs) -> None:
    response = requests.request(method=method, url=url, params=kwargs.get('params'))
    response.encoding = 'utf-8'
    re_patter = re.compile("http://www.(.*?).com", re.S)
    file_name = re_patter.findall(url)

    return set_dir(context=response.text, dir_name=file_name)


def set_dir(context, dir_name):
    with open(f'{dir_name[0]}.html', 'w', encoding='utf-8') as file:
        file.write(context)


set_request_context(method='get', url='http://www.baidu.com')

