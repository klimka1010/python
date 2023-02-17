def Treug(n, m, k):
    return n + m > k


def Max(a, b):
    if a > b: return a
    if a <= b: return b


for A in range(1, 1000):
    pod = True
    for x in range(1, 1000):
        if (not ((Treug(x, 11, 18) == ((not (Max(x, 5) > 15)))) or Treug(x, A, 5))) == False:
            pod = False
            break
    if pod:
        print(A)
