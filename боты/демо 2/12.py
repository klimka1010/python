k=0
for n in range (1,300):
    s=50*'С'+50*'Г'+50*'Н'

    while 'ГС' in s or 'НС' in s or 'ГН' in s:
        if 'ГС' in s:
            s=s.replace('ГС', 'СГ', 1)
        if 'НС' in s:
            s=s.replace('НС', 'СН', 1)
        if 'ГН' in s:
            s=s.replace('ГН', 'НГ', 1)
    # s=s.replace('>', '0')
    # sm=sum(int(x) for x in s)
    # if sm%7==0:
    #     k+=1
print(s[11],s[91],s[131])