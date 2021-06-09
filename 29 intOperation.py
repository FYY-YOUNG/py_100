# 给一个正整数，要求：一、求它是几位数，二、逆序打印出各位数字

from sys import stdout


n = int(input("请输入一个数:\n"))
l = len(str(n))

print("是 %d 位数：", l)

stdout.write('从个位往后： ')

for i in range(l):
    stdout.write(str(n % 10))
    stdout.write(' ')

    n = int(n / 10)



