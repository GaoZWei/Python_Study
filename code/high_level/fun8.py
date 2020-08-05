# filter

list_x = [1, 0, 1, 1, 1, 0, 1]
# list_u = ['a', 'B', 'c', "F", 'e']
r = filter(lambda x: True if x == 1 else False, list_x)
print(list(r))
