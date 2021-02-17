import sys


def multiply(n):
    if n == 0 or n == 1:
        return 1
    return n * multiply(n - 1)


def multiply_1(n):
    tmp = [None] * (n + 1)
    tmp[0], tmp[1] = 1, 1
    for i in range(2, n + 1):
        tmp[i] = tmp[i - 1] * i
    return tmp[n]


if __name__ == "__main__":
    # tmp = sys.stdin.readline().strip()
    # a, b = list(map(int, tmp.split()))
    # c = multiply(11)
    # print(c)
    # d = multiply_1(11)
    # print(d)
    l = list(map(lambda x: x * x, [1,3,5,7,9]))
    print(l)

    a = [1, 2, 3]
    b = tuple(a)
    print(type(b))
    print(b[1])
