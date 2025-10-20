def characters_in_range(first_character: str, second_character: str) -> list:
    chars_list = []
    for character in range(ord(first_character) + 1, ord(second_character)):
        chars_list.append(chr(character))
    return chars_list

first_char = input()
second_char = input()

list_of_chars = characters_in_range(first_char, second_char)
print(" ".join(list_of_chars))
