# -*- coding: UTF-8 -*-

def print_user_info( name ,  age  , sex = '男' ):
    # 打印用户信息
    print('昵称：{}'.format(name) , end = ' ')
    print('年龄：{}'.format(age) , end = ' ')
    print('性别：{}'.format(sex))
    return;

def print_user_info1( name ,  age  , sex = '男' , * hobby):
    # 打印用户信息
    print('昵称：{}'.format(name) , end = ' ')
    print('年龄：{}'.format(age) , end = ' ')
    print('性别：{}'.format(sex) ,end = ' ' )
    print('爱好：{}'.format(hobby))
    return;


def print_info( a , b = [] ):
    print(b)
    return b ;

# 调用 print_user_info 函数
if __name__ == '__main__':
    print_user_info( name = '两点水' ,age = 18 , sex = '女')
    print_user_info( name = '两点水' ,sex = '女', age = 18 )
    # 调用 print_user_info 函数
    print_user_info1('两点水', 18, '女', '打篮球', '打羽毛球', '跑步')

    result = print_info(1)

    result.append('error')

    print_info(2)
# 这是因为赋给形参的值是根据位置而赋值的。例如，def func(a, b=1) 是有效的，但是 def func(a=1, b) 是 无效 的。

