budget = int(input())

while True:
    price = input()

    if price == "End":
        print("You bought everything needed.")
        break

    budget -= int(price)

    if budget < 0:
        print("You went in overdraft!")
        break
