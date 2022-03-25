import json
with open('lesson05_07.txt', 'r', encoding='utf-8') as firm_file:
    try:
        firm_profit ={}
        firm_average_profit = {}
        firm_data = []
        while True:
            l = firm_file.readline().split()
            if not l:
                break
            firm_profit[l[0]] = float(l[2]) - float(l[3])
        count = 0
        average_profit = 0
        for v in firm_profit.values():
            if v >= 0:
                average_profit += v
                count += 1
        firm_average_profit["average_profit"] = round(average_profit / count, 2)
        firm_data.append(firm_profit)
        firm_data.append(firm_average_profit)
    except ValueError:
        print('ошибка')
with open('lesson05_07.json', 'w', encoding='utf-8') as firm_file_json:
    json.dump(firm_data, firm_file_json, indent=2)
    print('создан файл lesson05_07.json с указанием прибыльности/убытка каждой компании и средним значении прибыли не убыточных компаний')