k=0
x=[]

for i in range(14014, 49835+1):
    if i%13==5 and i%5!=0 and i%11!=0:
        k+=1
        x.append(i)

print(k, max(x))
