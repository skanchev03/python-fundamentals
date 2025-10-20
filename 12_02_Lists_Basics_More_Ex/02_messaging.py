sequence_of_numbers = input().split()
some_string_list = [x for x in input().strip()]
final_string = ""

for number in sequence_of_numbers:
    index = sum(int(digit) for digit in number)
    index = index % len(some_string_list)
    final_string += some_string_list.pop(index)

print(final_string)
