# 8 9 都在这里
import time

for i in range(1, 10):
    print()
    time.sleep(1)  # 暂停 1 秒

    for j in range(1, i+1):
        print ("%d*%d=%d" % (i, j, i*j), end=" " )
