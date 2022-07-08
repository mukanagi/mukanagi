# Словари - это неупорядоченные коллекции произвольных данных с доступлм по ключу

dictionary = {'House': 'Дом', 'Car': 'Машина',
               'Tree': 'Дерево', 'Road': 'Дорога',
               'River': 'Река'}

print(dictionary['Road'])

dictionary2 = dict(house='дом', car='машина', wife='жена')

# dict.fromkeys(список[, значение по умолчанию])

a = dict.fromkeys(['+7', '+5', '+4', '+33'], 'код страны')
print(a)

# d = {}
# d[True] = 'Истина'
# d[False] = 'Ложь'
# d['God'] = 111

# # del d[True]
# # print('abc' in d)
# # print(len(d))
# # print(d)

# # for k in d:
# #     print(k, d[k])

# # print(d.get('God'))

# print(d.setdefault('Badass'))
# print(d)
# del d['Badass']
# print(d)

# d.setdefault('Badass', 'Joe')
# print(d)

# d.pop('Badass')
# print(d)

# d.popitem() # удаляет произвольный элемент 
# print(d)

# d = {'Great Britain': 'London', 'Russia': 'Moscow',
#      'Ukrain': 'Kiev', 'Italy': 'Rome'}

# print(d.keys())
# print(d.values())

# print(type(d.keys()))

# for k, v in d.items():
#     print(v, 'is a capital of', k)

#d = {}
#for n in input("Введите числa через запятую: ").replace(",", " ").split():
#    n = int(n)
#    if n % 2 == 0:
#       d.setdefault(n, n**2)
#print(d)
