# 一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，
# 求它在第10次落地时，共经过多少米？
# 第10次反弹多高？

# 核心在于 每次落地后反跳回原高度的一半！！

height = [] # 每一次的反弹高度

hei = 100  # 起始高度
num = 10  # 次数

for i in range(1, num + 1):
    # 每次落地后反跳回原高度的一半
    hei /= 2
    height.append(hei)

print('它在第10次落地时，共经过 {0} 米'.format(sum(height) * 2 - height[9] * 2  + 100))
print('第10次反弹 {0} 米'.format(height[-1]))