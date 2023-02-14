# подсчет конкретной буквы 1
f = open('/Users/klimka1010/PycharmProjects/myFirstProject/боты/задачки/19-21/24var09-13.txt')
a = f.readline()
k = 0
for i in range(len(a)):
    if a[i] == 'Z':
        k += 1
print(k)

# подсчет конкретной буквы 2
f = open('/Users/klimka1010/PycharmProjects/myFirstProject/боты/задачки/19-21/24var09-13.txt')
a = f.readline()
print(a.count('Z'))

# подсчет максимальной последовательности одной буквы через количество таких последовательностей
f = open('/Users/klimka1010/PycharmProjects/myFirstProject/боты/задачки/19-21/24var09-13.txt')
a = f.readline()
print(a.count('Z' * 11))

f = open('/Users/klimka1010/PycharmProjects/myFirstProject/боты/задачки/19-21/24var09-13.txt')
a = f.readline()
k = 0
ans = 0
for i in range(len(a)):
    if a[i] == 'Z':
        k += 1
        if k > ans:
            ans = k
    else:
        k = 0
print(ans)

# сравнение с предыдущим символом для нахождения максимальной последовательности одной буквы
f = open('/Users/klimka1010/PycharmProjects/myFirstProject/боты/задачки/19-21/24var09-13.txt')
a = f.readline()
k = 1
ans = 0
for i in range(1, len(a)):
    if a[i] == a[i - 1]:
        k += 1
        if k > ans:
            ans = k
    else:
        k = 1
print(ans)

# количество одинакового символа через одну строчку
f = open('/Users/klimka1010/PycharmProjects/myFirstProject/боты/задачки/19-21/24var09-13.txt')
a = f.readline()
k = 1
ans = 1
i=0
while i<len(a):
    if a[i] == 'Z':
        k += 1
        if k > ans:
            ans = k
    else:
        k = 0
    i+=2
print(ans)