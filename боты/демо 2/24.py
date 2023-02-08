s=open('24.txt').readline()

s=s.replace('A', 'A').replace('E', 'A').replace('U', 'A').replace('B', 'B').replace('C', 'B').replace('D', 'B').replace('F', 'B')

while 'BAB' in s:
    s=s.replace('BAB', 'BA AB')

print(max(len(c) for c in s.split()))