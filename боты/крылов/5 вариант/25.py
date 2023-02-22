for i in range(10):
    for j in range(10):
        x = 12340708 + i*1000 + j*10
        if x % 31 == 0:
            print(x, x//31)