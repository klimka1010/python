f=open('24.txt').readline()

f=f.replace('CFE','1').replace('FCE', '1').replace('1',' 1 ')
print(f.count('1'))>