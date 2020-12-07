import requests, json, re
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
def setRequestContext(method, url, **kwargs) -> str:
    response = requests.request(method=method, url=url, params=kwargs.get('params'))
    response.encoding = 'utf-8'
    re_patter = re.compile('http://www.(.*?).com', re.S)
    fileName = re_patter.findall(url)

    return setDir(context=response.text, dirName=fileName)


def setDir(context, dirName):
    with open(f'{dirName[0]}.html', 'w', encoding='utf-8') as file:
        file.write(context)


setRequestContext(method='get', url='http://www.baidu.com')
