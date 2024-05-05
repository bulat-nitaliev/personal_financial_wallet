from model import Record, Correct

name_file = input('Введите имя файла с расширением для записей (необязательно - по умолчанию accounting.txt) ')
def menu():
    print('''
1. Вывести баланс
2. Добавить запись
3. Редактировать запись
4. Поиск
5. Выход
''')

    record = Record(name_file) if name_file else Record()
    correct = Correct()
    choice = input('Введите номер пункта меню: ')
    print()
    if choice == '1':
        balance, income, expense = record.get_balance()
        print(f'Текущий баланс: {balance}\nДоходы: {income}\nРасходы: {expense}')

    elif choice == '2':
        date = correct.is_date(input('Введите дату (YYYY-MM-DD): '))
        category = correct.is_category(input('Введите категорию (доход/расход): '))
        amount = correct.is_digit(input('Введите сумму цифрами: '))
        description = input('Введите описание (необязательно): ')
        record.add_record(date, category, amount, description)

    elif choice == '3':
        record_id = correct.current_id(int(input('Введите ID записи для редактирования: ')))
        date = correct.is_date(input('Введите дату (YYYY-MM-DD): '))
        category = correct.is_category(input('Введите категорию (доход/расход): '))
        amount = correct.is_digit(input('Введите сумму цифрами: '))
        description = input('Введите описание (необязательно): ')
        record.edit_record(record_id, date, category, amount, description)

    elif choice == '4':
        category = input('Введите категорию (необязательно): ')
        date = input('Введите дату (необязательно): ')
        c = input('Введите сумму (необязательно): ')
        amount = int(c) if c else 0

        description = input('Введите описание (необязательно): ')
        records = record.search_records(category, date, amount, description)
        print('Найденные записи:')
        print()
        for record in records:
            print('|'.join(record))

    elif choice == '5':
        exit()

    else:
        print('Неверный пункт меню')


while True:
    menu()