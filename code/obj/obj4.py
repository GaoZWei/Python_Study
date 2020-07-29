class Student():
    name = ''
    age = 0
    # 构造函数
    def __init__(self, name, age):
        self.name = name
        age = age


student1 = Student('哈哈', 12)  # 自动调用构造函数
print(student1.__dict__)
# 访问时会先访问实例变量，再在类中查找，再到父类中寻找
print(Student.__dict__)
