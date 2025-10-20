number_of_lines = int(input())
capacity = 255

for i in range(number_of_lines):
    liters = int(input())

    if capacity < liters:
        print("Insufficient capacity!")
        continue

    capacity -= liters

print(f"{255 - capacity}")
