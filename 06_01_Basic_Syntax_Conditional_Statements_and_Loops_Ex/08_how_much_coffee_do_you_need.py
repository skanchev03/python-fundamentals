coffee_count = 0

while True:
    command = input()

    if command == "END":
        break

    if command == "coding" or command == "dog" or command == "cat" or command == "movie":
        coffee_count += 1

    if command == "CODING" or command == "DOG" or command == "CAT" or command == "MOVIE":
        coffee_count += 2

if coffee_count > 5:
    print("You need extra sleep")
else:
    print(coffee_count)
