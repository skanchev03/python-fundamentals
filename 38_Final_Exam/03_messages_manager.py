capacity = int(input())
users = {}

while True:
    commands = input()
    if commands == "Statistics":
        break

    commands_list = commands.split("=")
    command = commands_list[0]

    if command == "Add":
        username = commands_list[1]
        if username in users:
            continue

        sent = int(commands_list[2])
        received = int(commands_list[3])
        users[username] = [sent, received]

    elif command == "Message":
        sender = commands_list[1]
        receiver = commands_list[2]

        if sender in users and receiver in users:
            users[sender][0] += 1
            if sum(users[sender]) == capacity:
                print(f"{sender} reached the capacity!")
                del users[sender]

            users[receiver][1] += 1
            if sum(users[receiver]) == capacity:
                print(f"{receiver} reached the capacity!")
                del users[receiver]

    elif command == "Empty":
        username = commands_list[1]
        if username == "All":
            users = {}
        else:
            if username in users:
                users.pop(username)

print(f"Users count: {len(users)}")

for user in users.items():
    username = user[0]
    sent, received = user[1]
    total = sent + received
    print(f"{username} - {total}")
