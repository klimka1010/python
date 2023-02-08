# считывание с файла
f=open('26.txt')
a=[]
for i in range (5):
    a.append(int((f.readline())))
a.sort()
print(a)
print(a[::-1])