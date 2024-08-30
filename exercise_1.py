pets = {}

while True:
    name = input("Введите имя питомца (для выхода введите пустую строку): ")

    if name == '':
        break
    else:
        kind = input('Введите вид питомца: ')
        age = int(input('Введите возраст питомца: '))
        owner_name = input('Введите имя владельца: ')

    pet = {'kind': kind, 'age': age, 'owner_name': owner_name}

    year = 'лет'

    if age % 10 == 1 and age != 11 and age % 100 != 11:
        year = 'год'
    elif 1 < age % 10 <= 4 and age != 12 and age != 13 and age != 14:
        year = 'года'

    pets[name] = pet

    print(
        f'Это {pet['kind']} по кличке "{name}". Возраст питомца: {pet['age']} {year}. Имя владельца: {pet['owner_name']}.')
