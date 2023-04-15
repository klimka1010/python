import itertools

k = 0
for i in itertools.product('012345', repeat=6):
    if i.count('2') == 1 and i.count('12') == 0 and i.count('21') == 0 and i.count('32') == 0 and i.count(
            '23') == 0 and i.count('52') == 0 and i.count('25') == 0 and i.count('72') == 0 and i.count(
            '27') == 0 and i.count('92') == 0 and i.count('29') == 0:
        k += 1

print(k)
