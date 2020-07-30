# 正则表达式
# 字符串匹配
import re

a = 'C0C++12java3python4Javascript'

r = re.findall('python', a)
print(r)

if len(r) > 0:
    print('字符串中有python')

