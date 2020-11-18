mix_list = ['1', 3, '5', 66, [23, '66', 'hello', '%%'], 34, '^^']
sum = 0
for i in mix_list:
    if type(i) is list:
        for j in i:
            if type(j) is int:
                sum += j
    if type(i) is int:
        sum +=i
print(sum)

sum = 0
for num in range(10, 21):
    print(num)
    if num % 2 != 0:
        sum += num
print(sum)


list_a = [1, 2, 3, 4, 5, 6, 7]
for i in list_a:
    # 第一次：i = 1 list_a = [2, 3, 4, 5, 6, 7]
    # 第二次：i = 2 list_a = [2, 4, 5, 6, 7]
    # 第三次：i = 3 list_a = [2, 4, 6, 7]
    # 第三次：i = 4 list_a = [2, 4, 6]
    list_a.remove(i)
print('list_a =', list_a)
list_a = [2, 4, 6]
print('修改一下')
