# 递归求 20！

def factorial(n):
    fn = 0
    if n == 0:
        fn = 1
    else:
        fn = n * factorial(n - 1)

    return fn

print(factorial(20))

for i in range(20):
    print("%d 的阶乘是 %d" % (i + 1,factorial(i + 1)))

