age = 18
name = 'klimka1010'
print('my name is ' + name + ', im ' + str(age) + ' years old and i love python!')
hello = 'my name is {0}, im {1} years old and i love python!'.format(name, age)
hello1 = 'my name is {fio}, im {old} years old and i love python!'.format(fio=name, old=age)
print(hello)

# f - строки    позволяют ссылаться на название переменных в строке
print(f'my name is {name}, im {age} years old and i love python!')
print(f'my name is {len(name.title())}, im {age + 10} years old and i love python!')


