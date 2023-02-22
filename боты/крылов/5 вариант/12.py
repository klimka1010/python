s = '2' * 2 + '1' * 2050 + '2' * 2

while '211' in s or '112' in s:
    s = s.replace('11', '1', 1)
    if '21' in s:
        s = s.replace('21', '12', 1)
    else:
        s = s.replace('12', '1', 1)

print(s)