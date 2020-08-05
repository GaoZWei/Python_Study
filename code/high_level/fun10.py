# 装饰器
# 特性 注解
import time


def f1():
    # print(time.time())  # unix 时间戳
    print('this is a function1')


def f2():
    # print(time.time())  # unix 时间戳
    print('this is a function2')


# f1()
# f2()


# 另外定义一个函数
def print_current_time(func):
    print(time.time())
    func()


print_current_time(f1)
print_current_time(f2)
