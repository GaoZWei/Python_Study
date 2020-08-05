# map+lanbda
list_x = [1, 2, 3, 4, 5, 6, 7, 8]
list_y = [1, 2, 3, 4, 5, 6, 7, 8]


# def squre(x):
#     return x*x

# for x in list_x:
#     squre(x)

r = map(lambda x,y: x*x+y, list_x,list_y)
print(list(r)) #元素个数取决于最小的个数
