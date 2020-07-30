import re

language = 'A84BC2313147890'

def convert(value):
    matched = value.group()  # 对象的group方法
    if int(matched) >= 6:
        return '9'
    else:
        return '0'

r = re.sub('\d', convert, language)
print(r)
