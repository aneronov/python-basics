class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return self.surname + ' ' + self.name


    def get_total_income(self):
        return self.income['wage'] + self.income['bonus']


a = Position('ivan', 'ivanov', 'assistant', 25000, 15000)
b = Position('pavel', 'pavlov', 'assistant', 55000, 5000)
print(a. get_full_name(), a.get_total_income())
print(b. get_full_name(), b.get_total_income())
