# print(413777 % 36)  // 29 вариант, XML -> YAML, Пятница
# https://codebeautify.org/xml-to-yaml# // перевод XML -> YAML
# https://jsonformatter.org/yaml-to-xml // перевод YAML -> XML

# открываем XML файл, лежит в папке с SC
xmlFile = open('file.xml')

# открываем XML файл, лежит в папке с SC, даем права для записи в файл
yamlFile = open("file.yaml", 'w')

# читаем файл, "разделяем" его построчно, записываем значения в "f"
f = xmlFile.read().split('\n')
for i in f:

    # если у нас "простая" команда, то заменяем "<" и ">" на "" и ":" соответственно
    if i.count('<') == 1:
        i = i.replace('<', '').replace('>', ':')

    # если команда "сложная", то заменяем всё что заменяется :-)
    if i.count('<') == 2:
        i = i.replace('<', '').replace('/week>', '').replace('/day>', '').replace('/lecture>', '').replace('/time>', '').replace('/prep>', '').replace('/form>', '').replace('>', ': ')

    # так же заменяем "неважные" для YAML команды
    if i.count('/employee:') == 1:
        i = i.replace('/employee:', '')
    if i.count('/employees:') == 1:
        i = i.replace('/employees:', '')

    # записываем получившийся файл в YAML
    print(i, file=yamlFile)


print('\n', 'Программа запущена успешно!')