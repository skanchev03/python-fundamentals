numbers = input().split(", ")
zero_counter = 0
final_list = []

for  number in numbers:
    if number == "0":
        zero_counter += 1
    else:
        final_list.append(int(number))

for i in range(zero_counter):
    final_list.append(0)

print(final_list)
