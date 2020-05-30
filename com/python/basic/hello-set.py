set1=set('hello')
set2=set(['p','y','y','h','o','n'])
print(set1)
print(set2)

# 交集 (求两个 set 集合中相同的元素)
set3=set1 & set2
print('\n交集 set3:')
print(set3)
# 并集 （合并两个 set 集合的元素并去除重复的值）
set4=set1 | set2
print('\n并集 set4:')
print(set4)
# 差集
set5=set1 - set2
set6=set2 - set1
print('\n差集 set5:')
print(set5)
print('\n差集 set6:')
print( set6)


# 去除海量列表里重复元素，用 hash 来解决也行，只不过感觉在性能上不是很高，用 set 解决还是很不错的
list1 = [111,222,333,444,111,222,333,444,555,666]
set7=set(list1)
print('\n去除列表里重复元素 set7:')
print(set7)

set8 = set(['111','hell','3333'])
print(set8)

#非零数值、非空字符串、非空 list 等，判断为 True，否则为 False。因此也可以这样写：

# 这时候我们可以结合 or 和 and 来使用。
# or （或）表示两个条件有一个成立时判断条件成功 and （与）表示只有两个条件同时成立的情况下，判断条件才成功。

input("请输入一个年份: ")

# 循环控制语句	描述
# break	在语句块执行过程中终止循环，并且跳出整个循环
# continue	在语句块执行过程中终止当前循环，跳出该次循环，执行下一次循环
# pass	pass 是空语句，是为了保持程序结构的完整性

# 使用 range(x) 函数，就可以生成一个从 0 到 x-1 的整数序列。
#
# 如果是 range(a,b) 函数，你可以生成了一个左闭右开的整数序列