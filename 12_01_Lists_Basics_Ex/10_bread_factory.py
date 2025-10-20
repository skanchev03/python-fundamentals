energy = 100
coins = 100
closed = False
events = input().split("|")

for event in events:
    event_number = event.split("-")
    event = event_number[0]
    current_coins = int(event_number[1])
    if event == "rest":
        current_energy = energy
        energy += current_coins
        if energy > 100:
            energy = 100
        print(f"You gained {energy - current_energy} energy.")
        print(f"Current energy: {energy}.")
    elif event == "order":
        if energy >= 30:
            energy -= 30
            coins += current_coins
            print(f"You earned {current_coins} coins.")
        else:
            energy += 50
            if energy > 100:
                energy = 100
            print("You had to rest!")
    else:
        if coins >= current_coins:
            print(f"You bought {event}.")
            coins -= current_coins
        else:
            print(f"Closed! Cannot afford {event}.")
            closed = True
            break
if not closed:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
