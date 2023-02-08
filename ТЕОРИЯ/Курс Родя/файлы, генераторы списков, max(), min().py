# # считывание первой строчки из файла
f = open('24.txt')
firstString = f.readline()
print(firstString)

# # считывание двух значений из первой строчки
f = open('24.txt')
x, y = map(int, f.readline().split())
print(x, y)

# записать все значения из файла в массив "а"
f = open('24.txt')
a = [int(x) for x in f]
print(a)

# записать все четные числа из массива
f = open('24.txt')
a = [int(x) for x in f if int(x) % 2 == 0]
print(a)
