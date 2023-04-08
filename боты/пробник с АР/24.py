f = open('24.txt')
s = f.readline()
k = 0
m = 0

for i in range(0, len(s) - 2):
    if s[i] == 'A' and s[i + 1] == 'BC' and s[i + 2] == 'BC':
        k += 1
        if k > m:
            m = k
        else:
            k = 0

for i in range(1, len(s) - 2):
    if s[i] == 'A' and s[i + 1] == 'BC' and s[i + 2] == 'BC':
        k += 1
        if k > m:
            m = k
        else:
            k = 0

for i in range(2, len(s) - 2):
    if s[i] == 'A' and s[i + 1] == 'BC' and s[i + 2] == 'BC':
        k += 1
        if k > m:
            m = k
        else:
            k = 0
