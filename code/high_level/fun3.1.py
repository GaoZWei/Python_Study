# 旅行者当前的位置x,打印实时位置
# 3=>3  5=>8 6=>14
# 先不用闭包

origin = 0


def go(step):
    global origin  #设置全局变量
    new_pos = origin+step
    origin = new_pos   #py认为左边的为局部变量
    return new_pos


print(go(2))
print(go(3))
print(go(6))
