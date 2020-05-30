
# 1、字符创创建迭代器对象
str1 = 'liangdianshui'
iter1 = iter(str1)

# 2、list对象创建迭代器
list1 = [1, 2, 3, 4]
iter2 = iter(list1)
for i in list1:
   print(i)
for i in iter2:
   print(i)

# 3、tuple(元祖) 对象创建迭代器
tuple1 = (1, 2, 3, 4)
iter3 = iter(tuple1)

# for 循环遍历迭代器对象
for x in iter1:
    print(x, end=' ')

print('\n------------------------')

# next() 函数遍历迭代器
while True:
    try:
        print(next(iter3))
    except StopIteration:
        break

print('\n'.join([' '.join ('%dx%d=%2d' % (x,y,x*y)  for x in range(1,y+1)) for y in range(1,10)]))
lsit1= [(x+1,y+1) for x in range(3) for y in range(5)]
print(lsit1)