def add(x, y):
    return x+y
add(1, 2)

# 匿名函数
f=lambda x, y:  x+y
print(f(1, 2))

# 三元表达式
# x > y?x: y  其他语言

# 条件为真返回的结果 if 条件判断 else 条件为假时的返回结果
x=1
y=2
r=x if x > y else y
print(r)
