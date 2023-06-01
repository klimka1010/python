s = '4'*60 + '6'*60 + '8'*60

while '46' in s or '84' in s or '86' in s:
    if '46' in s:
        s=s.replace('46', '64')
    if '84' in s:
        s=s.replace('84', '48')
    if '86' in s:
        s = s.replace('86', '68')

print(s)