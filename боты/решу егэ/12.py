s = '8' * 1000

while '999' in s or '888' in s:
    if '888' in s:
        s=s.replace('888', '9')
    else:
        s=s.replace('999', '8')

print(s)