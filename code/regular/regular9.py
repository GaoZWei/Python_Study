# re其他函数
import re

language = 'pythonC#javaphpC#'
# sub替换   0无限制替换
r = re.sub('C#', 'GO', language, 0)
# print(r)

# 需要重新创建
language1 = language.replace('C#', 'GO')
# print(language1)


# sub第二个参数可以是函数!!! 有用
def convert(value):
    matched = value.group()
    # print(value)
    return '!!'+matched+'!!'

r1 = re.sub('C#', convert, language, 0)
print(r1)
