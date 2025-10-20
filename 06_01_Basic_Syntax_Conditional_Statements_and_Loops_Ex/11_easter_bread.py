budget = float(input())
total_price = 0
flour_kg_price = float(input())
eggs_kg_price = flour_kg_price * 0.75
milk_kg_price = flour_kg_price * 1.25
loafs_counter = 0
colored_eggs_counter = 0

loaf_price = flour_kg_price + eggs_kg_price + milk_kg_price * 0.25

while True:
    total_price += loaf_price

    if total_price > budget:
        break

    loafs_counter += 1
    colored_eggs_counter += 3

    if loafs_counter % 3 == 0:
        colored_eggs_counter -= loafs_counter - 2

print(f"You made {loafs_counter} loaves of Easter bread! Now you have {colored_eggs_counter} eggs and {budget - total_price + loaf_price:.2f}BGN left.")
