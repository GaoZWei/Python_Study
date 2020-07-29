# 类将数据和操作封装在一起

class Student():
    name = 'gao'  # 意义不大
    age = 0
    # sum是一个班级的学生总数
    sum = 0

    # 构造函数
    def __init__(self, name, age):
        # 初始化对象属性
        self.name = name
        self.age = age
        # 类变量 实例变量
        # print('homework')
        # return 'student' 不建议return

    def print_file(self):  # 加self
        print('name'+self.name)
        print('age'+str(self.age))


student1 = Student('哈哈', 12)  # 自动调用构造函数
student2 = Student('呼呼', 18)
# student1.__init__()  # 显式调用构造函数

# a = student1.__init__()  # 显示调用构造函数
# print(a)
# print(type(a))
print(student1.name)
print(student2.name)
print(Student.name)
