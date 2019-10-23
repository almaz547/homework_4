date_birth_people = {'А.С.Пушкина': 1799, 'М.Ю.Лермонтова': 1814, 'С.А.Есенина': 1895, 'В.С.Высоцкого': 1938, 'В.Р.Цоя': 1962}
new_test = 'да'
while new_test == "да":
    answer_es = 0

    def year_day_birth(name, year):
        year_name = int(input(f'Введите год рождения {name}:  '))
        global answer_es
        if year_name == year:
            answer_es += 1
    for key, val in date_birth_people.items():
        year_day_birth(key, val)

    print(f'Количество правильных ответов:  {answer_es}')
    print(f'Количество неправильных отведов: {5 - answer_es}')
    print(f'Процент правильных ответов:  {answer_es * 100 / 5}')
    print(f'Процент неправильных ответов:  {(5 - answer_es) * 100 / 5}')
    new_test = input("Если хотите продолжить тест введите: да ,если не хотите, введите: нет:  ")
    while new_test != 'да' and new_test != 'нет':
        print("Введите либо: да , либо: нет !")
        new_test = input("Если хотите продолжить тест введите: да ,если не хотите, введите: нет !")
# На данный момент не вижу как зделать без глобал


