# group的概念  爬虫常用<span>
import re

s = 'life is short,i use python, i love python '

r = re.search('life(.*)python', s)
# print(r.group(1))  # group组号,默认是0

r1 = re.findall('life(.*)pytho(n)', s)
# print(r1) 

r2= re.search('life(.*)python(.*)python', s)
# print(r2.group(0))    返回全部
# print(r2.group(1))      返回第一组
# print(r2.group(2))    返回第二组
# print(r2.group(0,1,2))   #合并
# print(r2.groups())    只返回()中的匹配