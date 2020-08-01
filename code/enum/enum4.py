# 遍历
from enum import Enum


class VIP(Enum):
    YELLOW = 1
    GREEN = 1  # 将成为第一个的别名
    BLACK = 3
    RED = 4


class Common():
    YELLOW = 1


# print(VIP.GREEN)

# for v in VIP:  #第一种
#     print(v)
# for v in VIP.__members__:   #第二种
#     print(v)
# for v in VIP.__members__.items():  #第三种
#     print(v)
