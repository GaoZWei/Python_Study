import re
# re.match
# re.search
s = '84BC2313147890'
r = re.match('\d', s)  # 从字符串首字符匹配 返回对象 匹配一次
print(r)
r1 = re.search('\d', s)  # 搜索整个字符串 返回对象 匹配一次
print(r1.group())
print(r1.span())
r2 = re.findall('\d', s)  # 返回数组 匹配全部
print(r2)
