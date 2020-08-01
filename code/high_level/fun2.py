def f1():
    a = 10

    def f2():
        # a被认为是一个局部变量
        # a=20
        c = 20*a  # 只要引用外部就是闭包
    return f2


f = f1()
print(f)
