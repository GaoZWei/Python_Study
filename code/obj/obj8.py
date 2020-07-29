# 继承性
from obj9 import Human


class Student(Human):
    # sum = 0

    def __init__(self, school, name, age):
        self.school = school
        # Human.__init__(self, name, age)  # 子类调用父类方法 #必须传入self
        # 主流方式
        super(Student, self).__init__(name, age)
        # self.__score = 0
        # self.__class__.sum += 1

    def do_homework(self):
        super(Student,self).do_homework() #使用父类实例方法
        print('homework')


student1 = Student('大学', 'Gao', 18)
# print(Student.sum)
# print(student1.sum)
# print(student1.name)
# print(student1.age)
# student1.get_name()
student1.do_homework()
