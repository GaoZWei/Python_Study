class Test():
    def __len__(self):  # 两个方法影响方法值
        return 0  # 只能整型和波尔

    def __bool__(self):
        return False  # 只能bool型


test = Test()

if test:  # 防止误区,对象就是true是错的
    print('12')
else:
    print('no')

print(bool(None))
print(bool([]))
print(bool(test))

print(len(Test()))  # 必须在函数内部定义
