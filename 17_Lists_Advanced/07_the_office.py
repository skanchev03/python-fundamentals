employees_happiness = input().split()
factor = int(input())

post_factor_happiness = [int(x) * factor for x in employees_happiness]
average_happiness = sum(post_factor_happiness) // len(employees_happiness)
happy_counter = 0

for happiness in post_factor_happiness:
    if happiness > average_happiness:
        happy_counter += 1

if len(employees_happiness) // 2 <= happy_counter:
    print(f"Score: {happy_counter}/{len(employees_happiness)}. Employees are happy!")
else:
    print(f"Score: {happy_counter}/{len(employees_happiness)}. Employees are not happy!")
