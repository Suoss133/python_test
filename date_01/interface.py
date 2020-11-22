import requests

all_apis = {
    '主题首页': {
        'method': 'get',
        'url': '/topics',
        'params': {
            'page': 1,
            'tab': 'ask',
            'limit': 20,
            'mdrender': 'true'
        }
    },
    '主题详情': {
        'method': 'get',
        'url': '/topic/5fb8b2b306e8c0290c6c1370',
        'params': {
            'mdrender': 'true',
            'accesstoken': 'c46b1286-d392-402b-8c08-0edcb07d27ea',
        }
    },

    '新建主题': {
        'method': 'post',
        'url': '/topics',
        'params': {
            'accesstoken': 'c46b1286-d392-402b-8c08-0edcb07d27ea',
            'title': '11111',
            'tab': 'ask',
            'content': '121212121'
        }
    }

}


location = 'http://49.233.108.117:3000/api/v1'
for key,value in all_apis.items():
    result = requests.request(
        method=value['method'],
        url=location + value['url'],
        json=value['params'])
    print(result.json())
