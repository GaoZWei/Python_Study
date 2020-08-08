# -*- coding: utf-8 -*-

# ---while循环---
# CONDITION = True
# while CONDITION:
#     print(' i am  while')
# else:
#     pss

# ----for循环---
# a=['apple','orange','grape']
# for x in a:
#     print(x)

# ----for循环和break----
# b=[['apple','orange','grape'],(1,2,3)]
# for x in b:
#    for y in x:
#        if(y=='orange'):
#            break
#        print(y)
# else:
#     print('fruit is gone')

# ----break用法---
# c=[1,2,3]
# for x in c:
#     if x==2:
#         break

# ----for步长---
# 递增range(0,10,2),递减range(10,0,-2)
# for x in range(0, 10, 2):
#     print(x, end=' | ')


a = [1, 2, 3, 4, 5, 6, 7, 8]
for x in range(0, len(a), 2):
    print(x, end=' | ')

b = a[0:len(a):2]
print(b)
