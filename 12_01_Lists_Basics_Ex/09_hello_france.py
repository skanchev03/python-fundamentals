items_and_prices_string = input()
budget = float(input())
initial_budget = budget
items_and_prices_list = items_and_prices_string.split("|")
new_price = 0
new_price_list = []
profit = 0

for i in range(len(items_and_prices_list)):
    items_price = items_and_prices_list[i].split("->")
    item = items_price[0]
    price = float(items_price[1])

    if item == "Accessories" and 0 <= price <= 20.5 or item == "Shoes" and 0 <= price <= 35 or item == "Clothes" and 0 <= price <= 50:
        if budget < price:
            continue
        budget -= price
        new_price = price + 0.4 * price
        new_price_list.append(f"{new_price:.2f}")
        profit += new_price - price
print(" ".join(new_price_list))
print(f"Profit: {profit:.2f}")
if initial_budget + profit >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
