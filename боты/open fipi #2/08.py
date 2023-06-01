import itertools

k=1

for i in itertools.product('АЛПЦЯ', repeat=5):
    k+=1
    s=''.join(i)
    if s.count('А') <= 1 and s.count('Ц') == 2 and s.count('Л') == 0:
        print(k, s)
