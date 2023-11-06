












# 1
f = open('24.txt').readline()
a = f.split('Y')
b = []
for i in range(len(a)-150):
    b.append(sum([len(x) for x in a[i:i+151]]))

print(max(b)+150)
