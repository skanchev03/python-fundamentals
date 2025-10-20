def total_price(some_product: str, some_quantity: int):
    total = 0

    if some_product == "coffee":
        total = 1.5 * some_quantity
    elif some_product == "coke":
        total = 1.4 * some_quantity
    elif some_product == "water":
        total = 1 * some_quantity
    elif some_product == "snacks":
        total = 2 * some_quantity
    return f"{total:.2f}"

product = input()
quantity = int(input())

print(total_price(product, quantity))
