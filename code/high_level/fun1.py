# 闭包=函数＋环境变量(函数定义时候)
# 把函数调用的现场保存了
# 把函数作为参数,传到另外的函数里
# 把函数当做另外一个函数的返回结果


def curve_pre():
    a = 25

    def curve(x):
        return a*x*x

    return curve


a = 10
f = curve_pre() #从外部访问内部变量
print(f.__closure__)#闭包内容
print(f.__closure__[0].cell_contents)
# print(f(2))  # 优先调用
