# IntEnum
from enum import Enum
from enum import IntEnum, unique  # 每个数值必须都是int


@unique  # 会提示不能重复
class VIP(Enum):
    YELLOW = 1
    GREEN = 'str'
    BLACK = 1
    RED = 4

# 枚举类型不能实例化