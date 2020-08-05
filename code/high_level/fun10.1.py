# 装饰器解决问题
import time


def decorator(func):
    def wrapper(*args, **kw):  # *args 可变参数 **kw关键字参数
        print(time.time())
        func(*args, **kw)  # 通用调用,抽象
    return wrapper


# @语法糖
@decorator
def f1():
    print('this is a function1')


# 参数个数不同
@decorator
def f2(fun_name1, fun_name2):
    print('this is a function1'+fun_name1+fun_name2)


# 关键字参数
@decorator
def f3(fun_name1, fun_name2, **kw):
    print('this is a function1'+fun_name1+fun_name2)
    print(kw)


# f = decorator(f1)
# f()
print('-------------------')
f1()
print('-------------------')
f2('1', '2')
print('-------------------')
f3('1', '2', a=1, b=2, c=3)
