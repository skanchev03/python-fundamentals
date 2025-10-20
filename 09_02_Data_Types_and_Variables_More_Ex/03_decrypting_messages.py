key = int(input())
number_of_lines = int(input())
final_string = ""

for line in range(1, number_of_lines + 1):
    letter = input()

    new_letter = chr(ord(letter) + key)

    final_string += new_letter

print(final_string)
