from bs4 import BeautifulSoup

html = """
<html>
<head><title>story12345</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><span>westos</span><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister1" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
<p>story</P>
"""
soup = BeautifulSoup(html, 'html.parser')
# 格式化html，并补齐成对出现的标签
# print(soup.prettify())

# 获取标签中的内容
# print(soup.title)

# attrs获取标签中的属性，通过字典返回
# print(soup.p.attrs['class'])

# get获取标签中属性的值
# print(soup.p.get('class'))

# 查找符合条件的所有标签,返回list
aTagObj = soup.find_all('a')
# for item in aTagObj:
# print(item)

# class因为与python关键字冲突，所以使用class_
aTagObj = soup.find_all('a', class_='sister')
print(aTagObj)
# print()
for i in soup.children:
    print(i)

