# 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字
# 例如2+22+222+2222+22222(此时共有5个数相加)
# 几个数相加由键盘控制


from functools import reduce


Temp = 0
Sn = []
print("计算几位数相加，请输入 n：")
n = int(input('n = '))

print("请输入 a 的值：")
a = int(input('a = '))

for count in range(n):
    Temp = Temp + a
    a = a * 10
    Sn.append(Temp)
    print(Temp)

Sum = reduce(lambda x, y: x + y, Sn)  # 使用 lambda 匿名函数

print("计算结果为：", Sum)