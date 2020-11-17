# 字典推导
# DIAL_CODES = [(86, 'China'),
#               (91, 'India'),
#               (1, 'United States'),
#               (62,'Indonesia')]
#
# country_code = {country:code for code,country in DIAL_CODES}
# print(country_code)


# defaultdict使用
from collections import defaultdict
s = [('yellow',1),('blue',2),('yellow',3),('blue',4),('red',1)]
d= defaultdict()
for k,s in s:
    d[k].append(s)
print(d)
