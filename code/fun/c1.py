# -*- coding: utf-8 -*-
# 内置函数
# print()
# round()

# 1.功能性
# 2.隐藏细节
# 3.封装性

# def funcname(self, parameter_list):
#     pass

# 1.参数列表可以没有
# 2.return value None

import sys
sys.setrecursionlimit(10000)


def add(x, y):
    result = x+y
    return result


def print1(code):
    print(code)
    return

   # return 后面的不会执行
a = add(1, 2)
print1('python')
print(a)
