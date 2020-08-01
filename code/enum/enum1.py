# 枚举
from enum import Enum


class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4


class Common():
    YELLOW = 1


print(VIP.BLACK)  # 打印VIP.BLACK   枚举类型
print(VIP.BLACK.name)  # 打印BLACK    枚举名字
print(type(VIP.BLACK))  # VIP类型
print(type(VIP.BLACK.name))  # str类型
print(VIP.BLACK.value)  # 打印BLACK的值   枚举值
print(VIP['GREEN'])

# VIP.BLACK = 6  # 会报错
Common.YELLOW = 6  # 可修改

# 枚举类型,枚举名字,枚举值

# 遍历
for v in VIP:
    print(v)
