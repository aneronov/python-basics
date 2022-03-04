original_list = []
while True:
    input_data = input('Введите элемент списка(для завершения введите - break): ')
    if input_data == 'break':
        break
    original_list.append(input_data)
modified_list = list(original_list)
for i in range(0, len(modified_list) - 1, 2):
    modified_list[i], modified_list[i + 1] = modified_list[i + 1], modified_list[i]
print('исходный список: ', original_list)
print('изменённый список: ',modified_list)
