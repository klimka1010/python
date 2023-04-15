f = open('24_7094.txt').readline()
f = f.replace('A', '1').replace('U', '1').replace('C', '0').replace('D', '0').replace('F', '0')
print(f.count('01'))
