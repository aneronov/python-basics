class Date:
    def __init__(self, day, month, year):
        self.validate(day, month, year)


    @staticmethod
    def validate(day, month, year):
        if not 1 <= month <= 12 or year > 9999:
            print(f'неправильный формат даты (месяц - {month} или год - {year})')
        else:
            print(f'дата {day}.{month}.{year} введена корректно.')


    @classmethod
    def transformation(cls, data):
        try:
            z = [int(i) for i in data.split('-')]
            return cls(*z)
        except (TypeError, ValueError):
            print('неверный тип данных')

request = input('введите дату в виде строки формата «день-месяц-год»: ')
date = Date.transformation(request)




