# 利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来

from sys import stdout


def revertPrint(str,len):
    if len == 0:
        return
    else:
        stdout.write(str[len-1])
        stdout.write(' ')
        revertPrint(str,len - 1)

str = input('请输入 5 个字符:')
l = len(str)

stdout.write('反转结果是： ')
revertPrint(str,l)

