from datetime import datetime, date

class Correct:
  '''класс проверяет корректность ввода (валидация)
  пользователем значений (сумма, дата, выбор категории, id записи)
  в случае не верных значений рекурсивно повторяет проверку'''

  def is_digit(self, s:str)->str:
    '''проверяет чтобы пользователь ввел цифры, и возвращает строку
    в случае не верных значений рекурсивно повторяет проверку'''
    if s.isdigit():
      return s
    return self.is_digit(input('Введите сумму цифрами: '))

  def is_date(self, s:str)->str:
    '''проверяет чтобы пользователь ввел дату в формате (ГГГГ-MM-ДД), и возвращает строку
    в случае не верных значений рекурсивно повторяет проверку'''
    try:
      c = [int(i) for i in s.split('-')]
      return str(date(*c))
    except ValueError:
      self.is_date(input('Вы ввели не корректно пожайлуста в формате (ГГГГ-MM-ДД): '))

  def is_category(self, s:str)->str:
    '''проверяет чтобы пользователь ввел категорию , и возвращает строку
    в случае не верных значений рекурсивно повторяет проверку'''
    if s.lower() in ('доход','расход'):
      return s.lower()
    return self.is_category(input('Введите категорию доход или расход: '))


  def current_id(self, record_id:int)->int:
    '''проверяет чтобы пользователь ввел корректный номер записи , и возвращает строку
    в случае не верных значений рекурсивно повторяет проверку'''
    records = []
    with open('accounting.txt', 'r', encoding='utf-8') as f:
        for line in f:
            records.append(line.strip().split('|'))

    if record_id <= 0 or record_id > len(records):
      self.current_id(int(input('Неверный ID введите корректный ID записи для редактирования: ')))
    return record_id



class Record:
  '''класс для учета личных доходов и расходов
  создает файл txt имеет несколько методов
  1. Вывод баланса: Показать текущий баланс, а также отдельно доходы и расходы.
  2. Добавление записи: Возможность добавления новой записи о доходе или расходе.
  3. Редактирование записи: Изменение существующих записей о доходах и расходах.
  4. Поиск по записям: Поиск записей по категории, дате или сумме.
  '''
  def __init__(self, name_file='accounting.txt'):
    self.name_file = name_file

  def get_balance(self):
    '''Вывод баланса: Показать текущий баланс, а также отдельно доходы и расходы.'''
    balance = 0
    income = 0
    expense = 0
    try:
      with open(self.name_file, 'r', encoding='utf-8') as f:
          for line in f:
              date, category, amount, description = line.strip().split('|')
              amount = int(amount)
              if category == 'доход':
                  income += int(amount)
              elif category == 'расход':
                  expense += int(amount)

      balance = income - expense
      return balance, income, expense
    except FileNotFoundError:
        return (0,0,0)


  def add_record(self, date, category, amount, description):
    '''Добавление записи: Возможность добавления новой записи о доходе или расходе.'''
      with open(self.name_file, 'a', encoding='utf-8') as f:
          f.write(f'{date}|{category}|{amount}|{description}\n')


  def edit_record(self, record_id, date, category, amount, description):
    '''Редактирование записи: Изменение существующих записей о доходах и расходах.'''
      records = []
      with open(self.name_file, 'r', encoding='utf-8') as f:
          for line in f:
              records.append(line.strip().split('|'))

      records[record_id - 1] = [date, category, amount, description]

      with open(self.name_file, 'w', encoding='utf-8') as f:
          for record in records:
              f.write('|'.join(record) + '\n')


  def search_records(self, category=None, date=None, amount=None, description=None):
    '''метод осуществляет поиск по записям: Поиск записей по категории, дате или сумме.'''
      records = []
      with open(self.name_file, 'r', encoding='utf-8') as f:
          for line in f:
              record = line.strip().split('|')
              if (not category or record[1] == category) and (not date or record[0] == date) and (not amount or int(record[2]) == amount) and (not description or description in record[3]):
                  records.append(record)

      return records