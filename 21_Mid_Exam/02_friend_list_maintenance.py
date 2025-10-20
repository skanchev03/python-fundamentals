friends = input().split(", ")
blacklisted_counter = 0
lost_counter = 0

while True:
    command = input().split()

    if command[0] == "Report":
        break

    if command[0] == "Blacklist":
        name = command[1]
        if name in friends:
            index = (friends.index(name))
            friends[index] = "Blacklisted"
            print(f"{name} was blacklisted.")
            blacklisted_counter += 1
        else:
            print(f"{name} was not found.")

    if command[0] == "Error":
        index = int(command[1])
        if 0 <= index < len(friends):
            if friends[index] == "Blacklisted" or friends[index] == "Lost":
                continue
            else:
                print(f"{friends[index]} was lost due to an error.")
                friends[index] = "Lost"
                lost_counter += 1

    if command[0] == "Change":
        index = int(command[1])
        new_name = command[2]
        if 0 <= index < len(friends):
            print(f"{friends[index]} changed his username to {new_name}.")
            friends[index] = new_name

print(f"Blacklisted names: {blacklisted_counter}")
print(f"Lost names: {lost_counter}")
print(" ".join(friends))
