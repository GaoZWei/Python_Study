# 数量词 {1,10} 1-10个
# * 号代表前面的字符可以不出现，也可以出现一次或者多次
# + 号代表前面的字符可以出现一次或者多次
# ? 号代表前面的字符可以出现0次或者1次 (可以来去重)
import re
# 贪婪{1,10}  非贪婪{1,10}?
a = 'c0c++12 java3 &\npython4__javascript'
r = re.findall('[a-z]{1,10}', a)  # 匹配单词,默认贪婪匹配方式
# print(r)
b = 'c0c++1pythonn2 javna3 &\npython4__javapythoscript'
r1 = re.findall('python*', b)
print(r1)
r2 = re.findall('python+', b)
print(r2)
r3 = re.findall('python?', b)
print(r3)

