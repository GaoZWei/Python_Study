# 实例方法操作类变量+类方法+静态方法
class Student():
    sum1 = 0
    name = ''
    age = 0

    # 实例方法 固定放上self
    def __init__(self, name1, age):
        self.name = name1
        self.age = age
        # print(self.name)  # 读取self的name
        # print(name)  # 读取形参内容
        print(Student.sum1)  # 类变量访问way1
        self.__class__.sum1 += 1  # 类变量访问way2
        print('班级人数和'+str(self.__class__.sum1))

    # 实例方法
    def do_homework(self):
        print('homework')

    # 类方法
    @classmethod
    def plus_sum(cls):
        cls.sum1 += 1
        print(cls.sum1)

    # 静态方法
    @staticmethod
    def add(x, y):
        print(Student.sum1)
        print('this is static method')

student1 = Student('哈哈', 12)  # 自动调用构造函数
# student2 = Student('hehe', 13)
# print(student1.__dict__)   对象
# print(Student.sum1) 直接访问类变量
# Student.plus_sum()  # 类调用类方法
# student1.plus_sum()  # 对象调用类方法(不推荐)
student1.add(1, 2)  # 调用静态方法
Student.add(1, 2)  # 调用静态方法
