объект.метод(аргументы)

# значение это 3, 876, -25, True, 'string'
# индекс считается от нуля [0], [12]; [0, 23, 43]

a = [1, 55, 87, -124, 21]
a.append(100)  # добавляет значение любого типа в конец списка по значению ()
a.append(True)
a.insert(100, 5)  # вставляет значение 100 после пятого элемента
a.remove(43)  # удаляет первое найденное значение 43 считая, от начала списка

a.pop()  # удаляет последний элемент списка и возвращает его
a.pop(3)  # удаляет третий элемент [3] по индексу

a.clear()  # очистка списка полная

c=a.copy()
c=a[:]
c=list(a)

a.count(1)  # подсчет  
