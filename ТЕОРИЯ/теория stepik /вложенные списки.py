line = [1, 2, 3, 4, 5]
line2 = [line[:], line[:], line[:]]
line2[0] = [0] * 5
print(line2)
