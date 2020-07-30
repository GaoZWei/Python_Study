# 字符集[abc]或的关系
import re

a = 'abc,acc,adc,aec,afc,abc'

# 找到中间字符是c或者f的单词
r = re.findall('a[cfd]c', a)
r1 = re.findall('a[^cfd]c', a)
r2 = re.findall('a[c-f]c', a)


print(r)
