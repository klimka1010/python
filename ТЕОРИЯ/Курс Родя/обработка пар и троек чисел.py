a = [1, 2, 3, 4, 5]
for i in range(len(a) - 1):
    for j in range(i + 1, len(a)):
        if (a[i] + a[j]) % 2 == 0:
            print(a[i] + a[j], a[i], a[j])

for i in range(len(a) - 1):
    print(a[i], a[i + 1])

for i in range(len(a) - 2):
    print(a[i], a[i + 1], a[i + 2])

    # для пар чисел: len(a) - 1 для троек чисел: len(a) - 2
