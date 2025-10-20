wagons = [0 for _ in range(int(input()))]

while True:
    command = input().split()
    if command[0] == "End":
        break

    if command[0] == "add":
        people = int(command[1])
        wagons[-1] += people

    if command[0] == "insert":
        index = int(command[1])
        people = int(command[2])
        wagons[index] += people

    if command[0] == "leave":
        index = int(command[1])
        people = int(command[2])
        wagons[index] -= people

print(wagons)
