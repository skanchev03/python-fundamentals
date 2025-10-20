number_string = input()

number_string_list = number_string.split()
number_list = []

for i in range(len(number_string_list)):
    number = int(number_string_list[i]) * -1
    number_list.append(number)

print(number_list)
