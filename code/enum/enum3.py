# 比较运算
from enum import Enum


class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4


class Common():
    YELLOW = 1


result = VIP.GREEN == VIP.BLACK  # 等值比较
result1 = VIP.GREEN == 2
# result2 = VIP.GREEN > VIP.BLACK  # 不支持大小比较
result3 = VIP.GREEN is VIP.GREEN  # 支持身份比较
# result4 = VIP.GREEN is VIP1.GREEN  #false
print(result)
# print(result1)  # false
print(result3)  # true
