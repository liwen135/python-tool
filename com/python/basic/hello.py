#!/usr/bin/python3
print("Hello, World!")
for i in range(1,3):
    print(i)
# -*- coding: UTF-8 -*-
a = 257
b = 257
print(a == b)
print(a is b)
# 这里注意，比较操作符'is'的速度效率，通常要优于'=='。因为'is'操作符不能被重载，这样，Python 就不需要去寻找，程序中是否有其他地方重载了比较操作符，并去调用。执行比较操作符'is'，就仅仅是比较两个变量的 ID 而已。
#
# 但是'=='操作符却不同，执行a == b相当于是去执行a.__eq__(b)，而 Python 大部分的数据类型都会去重载__eq__这个函数，其内部的处理通常会复杂一些。比如，对于列表，__eq__函数会去遍历列表中的元素，比较它们的顺序和值是否相等。
# sting
str = 'Hello World!'

print(str)   # 输出完整字符串
print(str[0] )  # 输出字符串中的第一个字符
print(str[2:5] )  # 输出字符串中第三个至第六个之间的字符串
print(str[2:] )  # 输出从第三个字符开始的字符串
print(str * 2 )  # 输出字符串两次
print(str + "TEST")   # 输出连接的字符串

#列表  对于整型数字来说，以上a is b为 True 的结论，只适用于 -5 到 256 范围内的数字。比如下面这个例子：

list = ['runoob', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']

print (list)  # 输出完整列表
print(list[0])  # 输出列表的第一个元素
print(list[1:3])  # 输出第二个至第三个元素
print(list[2:] ) # 输出从第三个开始至列表末尾的所有元素
print(tinylist * 2)  # 输出列表两次
print(list + tinylist)  # 打印组合的列表
del list[3]

print (list)  # 输出完整列表
#存在与list中
print('runoob' in list)


# len(list)	列表元素个数
# max(list)	返回列表元素最大值
# min(list)	返回列表元素最小值
# list(seq)	将元组转换为列表
# list.append(obj)	在列表末尾添加新的对象
# list.count(obj)	统计某个元素在列表中出现的次数
# list.extend(seq)	在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
# list.index(obj)	从列表中找出某个值第一个匹配项的索引位置
# list.insert(index, obj)	将对象插入列表
# list.pop(obj=list[-1])	移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
# list.remove(obj)	移除列表中的一个元素（参数是列表中元素），并且不返回任何值
# list.reverse()	反向列表中元素
# list.sort([func])	对原列表进行排序