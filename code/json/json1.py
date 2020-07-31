# json是轻量级的数据交换格式
# 字符串是json的表现形式
import json

# json的键只能双引号
# json object==>python转化为字典   (反序列化)
json_str = '{"name":"gao","age":18}'
student = json.loads(json_str)  # py转换为字典
# print(type(student))
# print(student)
# print(student['name'])
# print(student['age'])

# json array==>python转化为列表
json_str1 = '[{"name":"gao","age":18,"flag":false},{"name":"gao","age":18}]'
student1 = json.loads(json_str1)
print(type(student1))
print(student1)
