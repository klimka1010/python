s=4**2020 + 2**2017 - 15
while True:
    bin(s)[2:]
    break
# print(str(s).count('1'))
print(bin(s).count('1'))