names_of_gifts = input()
gifts_list = names_of_gifts.split()

while True:
    command = input()

    if command == "No Money":
        break

    command_list = command.split()
    action = command_list[0]
    gift = command_list[1]

    if action == "OutOfStock":
        for i in range(len(gifts_list)):
            if gifts_list[i] == gift:
                gifts_list[i] = "None"

    elif action == "Required":
        index = int(command_list[2])
        if 0 <= index < len(gifts_list):
            gifts_list[index] = gift

    elif action == "JustInCase":
        gifts_list[-1] = gift

while "None" in gifts_list:
    gifts_list.remove("None")

print(" ".join(gifts_list))
