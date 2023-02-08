a = [2, 3, 5, 3, 2, 2]

a[0] = 4 # замена значения массива

b=list('klimka1010')   # массив всех значений

len(a) # длина массива
min(a) # минимальное значение массива
max(a) # максимальное значение массива
sum(a) # сумма элементов массива

sum(a) / len(a) # среднее значение массива

aSort=sorted(a) # сортировка по возрастанию
aSortReverse=sorted(a, reverse=True) # сортировка по возрастанию

x = 3 in a  # проверка вхождения указанного элемента в массив (True / False)

del a[0] # удаление элемента массива по индексу

print(x)


z,x,c = map(int, input().split()) # работа map(), заполняет введенные данные как массив в переменные
print(z,x,c)

x=list(map(int, input().split()))  # работа list(), заполняет данные в один массив
print(max(x), min(x), sum(x))

lst=list(map(int, input().split()))
lst.sort(reverse=True)
print(*lst)  # * - убирает [] фигурные скобки в ответе

cities = ["Москва", "Тверь", "Вологда"]
addCities=list(map(str,input().split()))
print(*cities, *addCities)
