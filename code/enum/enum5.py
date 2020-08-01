# 转换为枚举类型
from enum import Enum


class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4


class Common():
    YELLOW = 1


a = 1
print(VIP(a))  # 转换为枚举类型
