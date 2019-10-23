
cash_account = []                    # список денежных поступлений
sum_cash_account = 0                 # Сумма денег на счете
history = {}                         # История денежных операций
purchase_number = 0                  # Номер покупки
depositing_money_number = 0                 # Номер пополнения счета


while True:

    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')
    choice = input('Выберите пункт меню: ')
    def account_replenishment():           # 1  Внесение денег
        global sum_cash_account
        global depositing_money_number
        depositing_money = input('Пожалуйста внесите деньги для пополнения счета:  ')
        if not depositing_money.isdigit():
            account_replenishment()
        else:
            #print(depositing_money)
            cash_account.append(depositing_money)
            depositing_money = float(depositing_money)
            sum_cash_account += depositing_money
            depositing_money_number += 1
            history['Пополнение счета_' + str(depositing_money_number)] = depositing_money
            #print(cash_account)
            #print(sum_cash_account)
            #for key, val in history.items():
                #print(f'{key} = {val}')

    def purchases():                                             # 2 покупки
        purchase_price = input('Введите сумму покупки: ')
        global sum_cash_account
        global purchase_number
        if not purchase_price.isdigit():
            purchases()
        else:
            purchase_price = float(purchase_price)
            if purchase_price > sum_cash_account:
                print('Недостаточно денег на счете')
            else:
                name_purchase = input('Введите название покупки: ')
                sum_cash_account -= purchase_price
                purchase_number += 1
                history['Покупка_' + str(purchase_number) + '-' + name_purchase] = purchase_price

    def history_menu():                                   # 3 История покупок

        print('Ваши операции: ')
        for key, val in history.items():
            print(f'{key} => {val}')
        print(f'На вашем счете: {sum_cash_account} рублей')

    if choice == '1':
        account_replenishment()
    elif choice == '2':
        purchases()
    elif choice == '3':
        history_menu()

    elif choice == '4':
        break
    else:
        print('Неверный пункт меню')


'''Первое мое применение функций в программах,
 для их построения без global мои нейроны на данный момент не обучились. 
 Хорошо бы больше практики на прошедшии темы, и особенно четвертого урока.'''










