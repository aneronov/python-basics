product = []
j = 0
print('Для завершения ввода информации введите пустую строку в "наименование".')
while True:
    print('Введите информацию о товаре:')
    name = input('наименование: ')
    if name.isdigit():
        name = int(name)
    elif name == "":
        break
    price = input('цена: ')
    if price.isdigit():
        price = int(price)
    q_ty = input('кол-во: ')
    if q_ty.isdigit():
        q_ty = int(q_ty)
    unit = input('ед: ')
    if unit.isdigit():
        unit = int(unit)
    c = dict(наименование = name, цена = price, количество = q_ty, ед = unit)
    d = (j + 1, c)
    j += 1
    product.append(d)
key_list = []
temp_value_list = []
value_list = []
new_dict = {}
for i, j in enumerate(product[0][1]):
    key_list.append(j)
    for g in range(len(product)):
        temp_value_list.append(product[g][1].get(key_list[i]))
    value_list.append(temp_value_list)
    temp_value_list = []
    new_dict[key_list[i]] = value_list[i]
print('новая база данных:')
print(new_dict)