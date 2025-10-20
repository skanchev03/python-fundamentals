from operator import index

chat = []

while True:
    command = input().split()

    if command[0] == "end":
        break

    if command[0] == "Chat":
        message = command[1]
        chat.append(message)

    if command[0] == "Delete":
        message = command[1]
        if message in chat:
            chat.remove(message)

    if command[0] == "Edit":
        message = command[1]
        new_message = command[2]
        if message in chat:
            index = chat.index(message)
            chat[index] = new_message

    if command[0] == "Pin":
        message = command[1]
        if message in chat:
            chat.remove(message)
            chat.append(message)

    if command[0] == "Spam":
        for message in command:
            if message != "Spam":
                chat.append(message)

print("\n".join(chat))
