# 边界匹配 ^ $
import re

qq = '10001321301'

# 4-8位
r = re.findall('^\d{4,8}$', qq)  # 边界匹配 ^ $
# print(r)

a='10000001'
r1 = re.findall('000$', a)  # 边界匹配 ^ $
print(r1)

