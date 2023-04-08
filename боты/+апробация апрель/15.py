for P in range(19, 57):
    for Q in range(32, 85):
        def f(x, A, P, Q):
            return (not((x in A) and (x in Q))) <= (x in P)

print(min(A for A in range(0, 100) if all (f(x, A, P, Q) for x in range(1, 1000))))
