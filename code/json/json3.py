# 序列化  python=>json
import json
student = [
    {'name': 'gao', 'age': 18, 'flag': False},
    {'name': 'gao', 'age': 18}]

json_str = json.dumps(student)
print(json_str)
print(type(json_str))
