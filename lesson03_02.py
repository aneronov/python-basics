def pers_data(city, e_mail, name, surname, y_born, phone_num):
    print(f'{name} {surname} {y_born} года рождения, город проживания - {city}, адрес электронной почты - {e_mail}, номер телефона - {phone_num}')


pers_data(name = input('имя: '), surname = input('фамилия: '), y_born = input('год рождения: '), city = input('город проживания: '), e_mail = input('адрес электронной почты: '), phone_num = input('номер телефона: '))
