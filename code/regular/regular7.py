# 组()       []是或关系   ()是且关系
import re

a = 'pythonpythonpythonpythonpython'

r = re.findall('(python){3}', a)
print(r)
  