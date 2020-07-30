import re

a = 'C0C++12java3python4Javascript'

r = re.findall('\d', a)  # \d表示数字0到9
print(r)

b = re.findall('\D', a)  # \D表示非数字
print(b)
# 'python'普通字符
# '\d'元字符