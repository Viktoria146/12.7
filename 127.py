per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('Сумма вклада:'))
TKB = round((float(per_cent['ТКБ']) * money / 100), 2)
SKB = round((float(per_cent['СКБ']) * money / 100), 2)
VTB = round((float(per_cent['ВТБ']) * money / 100), 2)
SBER = round((float(per_cent['СБЕР']) * money / 100), 2)
deposit = [TKB, SKB, VTB, SBER]
print('Накопленные средства за год вклада:', deposit)
print(f"Максимальная сумма, которую вы можете заработать - {max(deposit)}")
