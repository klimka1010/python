# Текстовый файл 24.txt содержит последовательность из строчных и заглавных букв
# английского алфавита и цифр, всего не более 106 символов. Определите длину наибольшей
# убывающей подпоследовательности.    # 3
# 1 3 5 7 98 7 4
# 98 4

a=open('24.txt').readline()
k=0
m=0
q=0

for i in range(len(a)):
    if a[i-1]>a[i]:
        k+=1
        if k>m:
            k+=1
            m=k
            q=i
        else:
            k=0
print(m,k,q)