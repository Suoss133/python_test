import requests
import re


class CommonUtil:

    @classmethod
    def new_file(cls, file_content, dirName):
        if isinstance(dirName, list):
            with open(f'{dirName[0]}.html', 'w', encoding='utf-8') as file:
                file.write(file_content)
        if isinstance(dirName, str):
            with open(f'{dirName}.html', 'w', encoding='utf-8') as file:
                file.write(file_content)

    @classmethod
    def setRequestContext(cls, method: str, url: str, **kwargs) -> str:
        response = requests.request(method=method, url=url, params=kwargs.get('params'))
        response.encoding = 'utf-8'
        re_patter = re.compile('http://www.(.*?).com', re.S)
        fileName = re_patter.findall(url)

        return CommonUtil.new_file(file_content=response.text, dirName=fileName)

    @classmethod
    def run(cls):
        print('running')


CommonUtil.run()
