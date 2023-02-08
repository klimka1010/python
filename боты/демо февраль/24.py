s=open('24.txt').readline()
s=s.replace('O', 'A').replace('D', 'C').replace('F', 'C')
while 'CAAC' in s:
    s=s.replace('CAAC', 'CAA AAC')
print(max(len(c) for c in s.split()))