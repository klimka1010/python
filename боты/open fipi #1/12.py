s = '1' + 55 * '0'
while '1' in s:
    if '10' in s:
        s = s.replace('10', '001')
    else:
        s = s.replace('1', '00')

print(s.count('0'))
