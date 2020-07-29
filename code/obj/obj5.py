# 实力方法调用实例变量
lass Student():
    sum = 0
    name = ''
    age = 0

    # 实例方法 固定放上self
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(self.name)
        print(name)


student1 = Student('哈哈', 12)  # 自动调用构造函数
print(student1.__dict__)
# 访问时会先访问实例变量，再在类中查找，再到父类中寻找
# print(Student.__dict__)
