# 把一个列表分隔成几个小列表
a = [0, 2, 3, 4, 5, 6, 7, 8, 9, 10]

n = 2 #小列表 大小
print([ a[i : i + n] for i in range(0, len(a), n)])