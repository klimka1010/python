s = 5 ** 2019 - 5 ** 1019 + 25 ** 600 - 125
k=0
t=''

while s > 0:
    t+=(str(s%5))
    s=s//5
print(t.count('4'))

