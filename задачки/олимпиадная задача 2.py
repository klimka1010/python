#5
# -4, 3, -5, 2, 5
# massive = [1, 2, 3, 4, 5]

print('Введите размер массива: ')
volume = int(input())

print('Введите значения массива: ')
massive = list(map(int, input().split()))

if volume != len(massive):
    print('Ввод неверен! \n')


if volume == len(massive):
    print('Ввод верен! \n')
    print('Ваш массив: ', massive)
    firstMax = massive[0]
    secondMax = massive[0]


    for i in massive:
        if i > firstMax:
            firstMax = i

    for i in massive:
        if i > secondMax and i != firstMax:
            secondMax = i


    answer = [firstMax, secondMax]
    answer.sort()
    print('Ваш ответ: ', answer)