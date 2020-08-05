# reduce 连续计算,连续调用lambda
from functools import reduce
list_x = [1, 2, 3, 4, 5, 6, 7, 8]
r = reduce(lambda x, y: x+y, list_x,10) #10是初始值
print(r)

# (((1+2)+3)+4)+5....


# 旅行者x,y