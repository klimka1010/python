time = {'0': 0}

for i in open('22.txt'):
    i = i.replace(';', ' ')
    s = s.split()
    time[s[0]] = int(i[1]) + max(time[k] for k in s[2:])

print(max(time.values()))