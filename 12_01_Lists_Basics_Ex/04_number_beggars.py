integer_string = input()
beggars_count = int(input())
money_list = integer_string.split(", ")
beggars_profit_list = []

for i in range(beggars_count):
    profit = 0
    for j in range(i, len(money_list), beggars_count):
        profit += int(money_list[j])
    beggars_profit_list.append(profit)

print(beggars_profit_list)
