# массивы (списки)
a = []
a.append(6)
print(a)

a = []
n = int(input())
while a < 10  # если не знаем сколько нам нужно пройти по циклу
    for i in range(n):  # если знаем
        a.append(int(input()))
print(a)

lines = []
for i in range(n):
    lines[i]


# функции
def f(x):
    return x ** 2


f(4)  # = 16

# файлы
inputFile = open('file.txt', 'r')  # r - read, w - write
lines = inputFile.readlines()
out = ''
for line in lines:
    a, b = line.split(' ')
    a, b = int(a), int(b)
    sum = a + b
    out += str(sum) + '\n'
outputFile = open('out.txt', 'w')
outputFile.write(out)

inputFile = open('17-3.txt', 'r')
lines = inputFile.readlines()
a = []
for i in range(1):
    a = [lines]
print(a[1])
