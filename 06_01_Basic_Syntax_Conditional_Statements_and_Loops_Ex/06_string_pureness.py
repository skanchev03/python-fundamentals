n = int(input())

for i in range(n):
    pure = True
    string = input()

    for j in range(len(string)):
        if string[j] == "," or string[j] == "." or string[j] == "_":
            print(f"{string} is not pure!")
            pure = False
            break

    if pure:
        print(f"{string} is pure.")
