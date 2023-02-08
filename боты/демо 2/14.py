for x in '0123456789abcdefg':
    a = int(f'100{x}', 5)  == int(f'200', 4)
    if a%7==0:
        print(x, a//7)

        # a = int(f'100', 5) + int(({x})) = int(f'200', 4)
