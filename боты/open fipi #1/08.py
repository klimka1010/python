import itertools

k = 0
for i in itertools.product('012345', repeat=6):
    s = ''.join(i)  # !!! s=''.join(i) !!!
    if s[0] != '0' and s.count('2') == 1 and s.count('12') == 0 and s.count('21') == 0 and \
            s.count('32') == 0 and s.count('23') == 0 and \
            s.count('52') == 0 and s.count('25') == 0:
        k += 1

print(k)