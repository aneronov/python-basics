some_list = [10, 7, 5, 4, 3]
new_list = list(some_list)
while True:
    new_one = input(f'Введите новый элемент рейтинга {some_list} больше 0: ')
    if new_one.isalpha():
        print('ошибочка!')
        continue
    if int(new_one) <= 0:
        print('ошибочка!')
        continue
    new_one = int(new_one)
    break
for i in range(len(new_list) - 1, -1, -1):
    if new_list[i] >= new_one:
        new_list.insert(i + 1, new_one)
        break
if new_list[0] < new_one:
    new_list.insert(0, new_one)
print("до: ", some_list)
print("после: ", new_list)