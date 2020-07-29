# 成员可见性
class Student():
    sum1 = 0

    # 实例方法 固定放上self
    def __init__(self, name1, age):
        self.name = name1
        self.age = age
        self.__score = 0  # __是私有
        self.__class__.sum1 += 1

    # 实例方法
    def do_homework(self):
        print('homework')

    def marking(self, score):
        if(score < 0):
            score = 0
            return '不能负分'
        self.__score = score
        print(self.name+'分数为'+str(self.__score))

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


student1 = Student('Gao', 18)

result = student1.marking(159)
print(result)
student1.__score = -1  # 新添加实例变量

print(student1.__dict__)
print(student1._Student__score)#间接访问私有变量
