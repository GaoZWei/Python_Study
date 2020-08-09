# 列表推导式
# set,dict,元组也可以被推导
a = [1, 2, 3, 4, 5, 6, 7, 8]

b = [i*i for i in a]
b = [i**2 for i in a]  # 两者等价
print(b)

b1 = [i**2 for i in a if i >= 5]
print(b1)

a1 = {1, 2, 3, 4, 5, 6, 7, 8}
b2 = {i**2 for i in a1 if i >= 5}
print(b2)

a3 = (1, 2, 3, 4, 5, 6, 7, 8)
b3 = (i**2 for i in a1 if i >= 5)
print(b3)  #--有问题  # 元组不可变
