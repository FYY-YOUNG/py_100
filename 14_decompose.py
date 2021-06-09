# 给定一个正整数，将给定的正整数分解质因数；
# 例如：输入90,打印出90=2*3*3*5。

n = int(input('请输入需要分解的正整数:'))

# 列表存放 质因数
lt = []
m = n
while n > 1:
    for i in range(2,n+1):
        if n%i==0:
            # n 替换一下分解后的新值
            n = n//i
            # 存放 质因数
            lt.append(str(i))
            break

if len(lt) == 1:
    print(m,'=',m)
else:
    s = '×'.join(lt)
    print(m,'=',s)
