quantity_of_decorations = int(input())
days_left_until_christmas = int(input())
total_cost = 0
spirit_gained = 0

for days in range(1, days_left_until_christmas + 1):
    if days % 11 == 0:
        quantity_of_decorations += 2
    if days % 2 == 0:
        total_cost += quantity_of_decorations * 2
        spirit_gained += 5
    if days % 3 == 0:
        total_cost += quantity_of_decorations * 8
        spirit_gained += 13
    if days % 5 == 0:
        total_cost += quantity_of_decorations * 15
        spirit_gained += 17
    if days % 10 == 0:
        total_cost += 23
        spirit_gained -= 20
    if days % 15 == 0:
        spirit_gained += 30

if days_left_until_christmas % 10 == 0:
    spirit_gained -= 30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {spirit_gained}")
