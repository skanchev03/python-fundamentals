from math import ceil, floor

budget = float(input())
students = int(input())
price_flour = float(input())
price_eggs = float(input())
price_apron = float(input())

total_flour = students - floor(students / 5)
total_eggs = students * 10
total_aprons = ceil(students + students * 0.2)\

total_price = price_flour * total_flour + price_eggs * total_eggs + price_apron * total_aprons

if total_price <= budget:
    print(f"Items purchased for {total_price:.2f}$.")
else:
    print(f"{total_price - budget:.2f}$ more needed.")
