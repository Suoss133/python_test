# def consumer():
#     print('[CONSUMER] start')
#     r = 'start'
#     while True:
#         n = yield r
#         if not n:
#             print('n is empty')
#             continue
#         print('[CONSUMER] Consumer is consuming %s' % n)
#         r = '200 ok'
#
#
# def producer(c):
#     start_value = c.send(None)
#     print(start_value)
#     n = 0
#     while n < 3:
#         n += 1
#         print('[PRODUCER] Producer is producing % d' % n)
#         r = c.send(n)
#         print('[PRODUCER] Consumer return: %s' % r)
#     c.close()
#
#
# c = consumer()
# producer(c)


# from collections.abc import Iterable
#
#
# def flatten(items, ignore_types=(str, bytes)):
#     for x in items:
#         if isinstance(x, Iterable) and not isinstance(x, ignore_types):
#             yield from flatten(x)
#         else:
#             yield x
#
#
# items = [1, 2, ['Dave', 4, [5, 6], 7], 8]
# for x in flatten(items):
#     print(x)


# list_num = [["k", ["qwe", 20, {"k1": ["tt", 3, "1"]}, {"k2": [100, 99]}, 89], "ab"]]
#
#
# def fotlat(items, ig=(str, bytes)):
#     for item in items:
#         if isinstance(item, Iterable) and not isinstance(item, ig):
#             yield from fotlat(item)
#             if isinstance(item, dict):
#                 yield from item.values()
#         else:
#             yield [item]
#
#
# def update_dict(value, orlder):
#     global list_num
#     for i in fotlat(list_num):
#         if isinstance(i ,list):
#             for x in i:
#                 if value == x:
#                     index = i.index(value)
#                     i[index] = orlder
#
#
# update_dict(100, 'updatee1')
# print(list_num)



import asyncio

# def test(n):
#     i = 0
#     while i < n:
#         yield i
#         i += 1
#
#
# @asyncio.coroutine
# def test_yield_from(n):
#     print('test_yield_from start')
#     yield from test(n)
#     print('test_yield_from end')
#
#
# # for i in test_yield_from(3):
# #     print(i)
# print(asyncio.iscoroutinefunction(test_yield_from))
#
# print(asyncio.iscoroutine(test_yield_from(3)))

#
# @asyncio.coroutine
# def compute(x, y):
#     print("Compute %s + %s ..." % (x, y))
#     yield from asyncio.sleep(1.0)
#     return x + y
#
#
# @asyncio.coroutine
# def print_sum(x, y):
#     result = yield from compute(x, y)
#     print("%s + %s = %s" % (x, y, result))
#
#
# loop = asyncio.get_event_loop()
# print("start")
# # 中断调用，直到协程执行结束
# loop.run_until_complete(print_sum(1, 2))
# print("end")
# loop.close()

from collections.abc import Iterable

dic = {'name': 'Tom', 'age':
    [{'resourceType': 'BANNER_GROUP',
      "resourceId": 'null',
      "bffBannerGroup": {
          "id": 39,
          "title": "商城促销",
          "elements": '',
          "displayMargin": True,
          "displayPadding": True,
          "rotational": False,
          "slidable": False,
          "position": "HOME_PAGE_TOP",
          "titleLink": {
              "miniProgramUrl": '',
              "h5Url": ''}}}]}


def flatten_dic(items: dict, ignore_types=(str, bytes)):
    for key, value in items.items():
        if isinstance(value, dict):
            yield from flatten_dic(value)
        elif isinstance(value, list):
            yield from flatten_list(value)
        else:
            yield {key: value}


def flatten_list(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, dict) and not isinstance(x, ignore_types):
            yield from flatten_dic(x)
        else:
            yield x


for key in flatten_dic(dic):
    print(key)
