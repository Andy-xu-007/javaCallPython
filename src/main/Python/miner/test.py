import sys


def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num==1:
        return product
    return fact_iter(num-1, num*product)

def fact_1(n):
    if n==1:
        return 1
    return n * fact(n - 1)

def climbStairs(n):
    if n==1 :
        return 1
    if n==2:
        return 2
    return climbStairs(n-1) + climbStairs(n-2)

def climbStairs_1(n):
    res = [None] * (n)
    res[0] = 1
    res[1] = 2
    for i in range(2, (n)):
        res[i] = res[i-1] + res[i-2]
    return res[n-1]

def dp_fib(n):
    res = [None] * (n + 1)
    res[0] = res[1] = 1
    for i in range(2, (n + 1)):
        res[i] = res[i-1] + res[i-2]
    return res[n]



if __name__ == "__main__":
    # tmp = sys.stdin.readline().strip()
    # a, b = list(map(int, tmp.split()))
    c = climbStairs(10)
    print(c)
    d = climbStairs_1(10)
    print(d)
    # e = dp_fib(5)
    # print(e)


    # a = fact_1(10)
    # print(a)
    # b = fact(10)
    # print(b)

class Student():

    def __init__(self, name, age):
        self.name = name
        self.age = age

st = Student("andy", 13)
print(st.age)

