def palindrome_integers(some_number: int) -> bool:
    some_number_as_str = str(some_number)
    if some_number_as_str == some_number_as_str[::-1]:
        return True
    return False


sequence_of_numbers = list(map(int, input().split(", ")))

for number in sequence_of_numbers:
    print(palindrome_integers(number))
