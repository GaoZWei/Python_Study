# 概括字符集
import re

a = 'C0C++12 java3 &p\nython4__Javascript'
r = re.findall('\d', a)  # 匹配数字
r1 = re.findall('[0-9]', a)  # 匹配数字
r2 = re.findall('\w', a)  # 匹配单词字符和数字
r3 = re.findall('[A-Za-z0-9_]', a)  # 匹配单词字符和数字
r4 = re.findall('\W', a)  # 匹配非单词字符
r5 = re.findall('\s', a)  # 匹配空白字符,制表符
                         # . 匹配除换行符\n之外所有字符 
# print(r)
# print(r1)
# print(r2)
# print(r3)
# print(r4)
print(r5)
