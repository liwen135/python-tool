# -*- coding: UTF-8 -*-
def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

# 引用函数
for x in fibon(10):
    print(x , end = ' ')

gen= (x * x for x in range(10))
gen1= [x * x for x in range(10)]

print('gen1----------')
for num  in  gen1 :
	print(num)
    
print('gen---------')
for num  in  gen :
	print(num)

# -*- coding: UTF-8 -*-
def odd():
    print ( 'step 1' )
    yield ( 1 )
    print ( 'step 2' )
    yield ( 3 )
    print ( 'step 3' )
    yield ( 5 )

o = odd()
print( next( o ) )
print( next( o ) )
print( next( o ) )