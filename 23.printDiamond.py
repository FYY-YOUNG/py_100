
from sys import stdout
for i in range(4):  # 前四行
    for j in range(2 - i + 1): # 第一行为例 i=0 先打印 3空格 再打印 1个 *
        stdout.write(' ')
    for k in range(2 * i + 1):
        stdout.write('*')
    print('')

for i in range(3):  # 后三行
    for j in range(i + 1):
        stdout.write(' ')
    for k in range(4 - 2 * i + 1):
        stdout.write('*')
    print('')