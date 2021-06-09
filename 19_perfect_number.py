# 一个数如果恰好等于它的因子之和，这个数就称为"完数"。
#
# 例如 6=1＋2＋3.
#
# 编程找出1000以内的所有完数

# 标准输出
from sys import stdout

for j in range(2, 1001):
    k = []  # 存放因子
    n = -1  # 因子的索引 输出时使用
    s = j   # 暂存 j 的原始值

    for i in range(1, j):   # 找因子
        if j % i == 0:
            n += 1  # 记录对应因子的索引
            s -= i      # 判断 j 是否等于因子之和
            k.append(i)

    if s == 0: # 是元数
        stdout.write(str(j))     # 不会默认换行
        stdout.write(' = ')

        for i in range(n):  # 到 n  不是 n+1；为了最后一个输出
            stdout.write(str(k[i]))
            stdout.write(' + ')
        print(k[n])     # 注意此处对于 + 与 最后一个因子的输出处理 ，n 为索引