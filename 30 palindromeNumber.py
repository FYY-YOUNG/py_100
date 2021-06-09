# 一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。

from sys import stdout

n = int(input("请输入一个 5 位数:\n"))
s = str(n)

flag = False

if len(s) != 5:
    stdout.write('不是 5 位数 ')
else:
    for i in range(len(s) // 2):
        if s[i] != s[-i - 1]:
            flag = False
            break
        else:
            flag = True

if (flag):
    print("是 一个回文数!" )
else:
    print("不是 一个回文数!" )


