while True:
    string = input()

    if string == "End":
        break

    if string == "SoftUni":
        continue

    for i in range(len(string)):
        print(string[i] + string[i], end="")
    print()
