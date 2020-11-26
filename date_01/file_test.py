import os

file = open('/pythonFile/test_python/date_01/1.txt')
# print(file.read())
try:
    while True:
        line = file.readline()
        if line:
            print(line)
        else:
            break
finally:
    file.close()