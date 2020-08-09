# 字典的列表推导式

students = {
    '喜小乐': 18,
    '哈哈': 12,
    '大大': 13
}

b = {value: key for key, value in students.items()}
print(b)

b1 = (key for key, value in students.items())  # 元组不可变
for x in b1:
    print(x)
