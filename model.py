from datetime import datetime, date

class Correct:
  def is_digit(self, s:str)->int:
    if s.isdigit():
      return s
    return self.is_digit(input('Введите сумму цифрами: '))

  def is_date(self, s:str)->str:
    try:
      c = [int(i) for i in s.split('-')]
      return str(date(*c))
    except ValueError:
      self.is_date(input('Вы ввели не корректно пожайлуста в формате (ГГГГ-MM-ДД): '))

  def is_category(self, s:str)->str:
    if s.lower() in ('доход','расход'):
      return s.lower()
    return self.is_category(input('Введите категорию доход или расход: '))


  def current_id(self, record_id:int)->int:
    records = []
    with open('accounting.txt', 'r', encoding='utf-8') as f:
        for line in f:
            records.append(line.strip().split('|'))

    if record_id <= 0 or record_id > len(records):
      self.current_id(int(input('Неверный ID введите корректный ID записи для редактирования: ')))
    return record_id



class Record:

  def get_balance(self):
    balance = 0
    income = 0
    expense = 0
    try:
      with open('accounting.txt', 'r', encoding='utf-8') as f:
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

  # Функция для добавления записи
  def add_record(self, date, category, amount, description):
      with open('accounting.txt', 'a', encoding='utf-8') as f:
          f.write(f'{date}|{category}|{amount}|{description}\n')

  # Функция для редактирования записи
  def edit_record(self, record_id, date, category, amount, description):
      records = []
      with open('accounting.txt', 'r', encoding='utf-8') as f:
          for line in f:
              records.append(line.strip().split('|'))

      records[record_id - 1] = [date, category, amount, description]

      with open('accounting.txt', 'w', encoding='utf-8') as f:
          for record in records:
              f.write('|'.join(record) + '\n')

  # Функция для поиска записей
  def search_records(self, category=None, date=None, amount=None, description=None):
      records = []
      with open('accounting.txt', 'r', encoding='utf-8') as f:
          for line in f:
              record = line.strip().split('|')
              if (not category or record[1] == category) and (not date or record[0] == date) and (not amount or int(record[2]) == amount) and (not description or description in record[3]):
                  records.append(record)

      return records