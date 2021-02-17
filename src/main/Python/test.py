class Solution:
    def read(self, file, str):
        f = open(file, 'r')
        l = []
        line = 1
        str_long = len(str)
        for i in f.readlines():
            num = 0
            for j in range(len(i)):
                if str == i[j:j+str_long]:
                    num += 1
            if num:
                l.append([line, num])
            line += 1
        f.close()
        return l


solution = Solution()
solution.read()
