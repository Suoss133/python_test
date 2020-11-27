import os, requests

# file = open('/pythonFile/test_python/date_01/1.txt')
# # print(file.read())
# try:
#     while True:
#         line = file.readline()
#         if line:
#             print(line)
#         else:
#             break
# finally:
#     file.close()

# file = os.listdir('.')
# for x in file:
#     base_file = os.path.splitext(x)[1]
#     print(base_file)


# with open('1.png','wb') as file:
#     file.write(response.content)

url_image = {'one':'https://dss1.baidu.com/6ONXsjip0QIZ8tyhnq/it/u=2333090299,850498900&fm=5',
       'two':'https://dss0.baidu.com/6ONWsjip0QIZ8tyhnq/it/u=2247692397,1189743173&fm=5',
       'three':'https://dss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=1781104810,1859623527&fm=26&gp=0.jpg'}
for key,value in url_image.items():
    response = requests.get(value)
    with open(f'{key}.png','wb') as file:
        file.write(response.content)


