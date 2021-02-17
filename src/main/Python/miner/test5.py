class Test1:
    a = -4
    b = -4
    c = 400
    e = 400
    d = -1234

class Test2:
    a = -4
    c = 400
    d = -1234

t1 = Test1()
t2 = Test2()
print(t1.a is t1.b) # True # 同一个代码块中的相同小整数为同一对象
print(t1.c is t1.e) # True # 同一个代码块中的相同大整数为同一对象
print(t1.a is t2.a) # True # 不同两个代码块中的相同小整数为同一对象
print(t1.c is t2.c) # False # 不同两个代码块中的相同大整数内容相同，不是同一对象
print(t1.d is t2.d)