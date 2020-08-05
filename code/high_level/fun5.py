# map 映射
list_x = [1, 2, 3, 4, 5, 6, 7, 8]


def squre(x):
    return x*x

for x in list_x:
    squre(x)

r=map(squre,list_x)
print(list(r))