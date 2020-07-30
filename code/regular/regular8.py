# re.findall的第三个参数
import re

language = 'pythonC#\njavaphp'

r = re.findall('c#.{1}', language, re.I | re.S)  # re.I让正则忽略大小写
print(r)                                         # re.s让正则忽略换行符\n
