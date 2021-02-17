import sys

def sum(n):
    tmp = [None] * (n + 1)
    tmp[0] = 1
    tmp[1] = 1
    for i in range(2, n+1):
        tmp[i] = tmp[i-1] * i
    return tmp[n]

if __name__ == "__main__":
    # tmp = sys.stdin.readline().strip()
    # a, b = list(map(int, tmp.split()))
    # a = [2,2,1,1,4,4,7]
    # b = set(a)
    # for i in b:
    #     a.remove(i)
    # x = [i for i in b if i not in a][0]
    # print(x)
    # print(y)
    a = "aba"
    b = set(list(a))
    z = len(a) - len(b)
    q = sum(len(a)) - 2 ** z
    print(q)


