def absolute_value_list(sequence: str) -> list:
    sequence_of_numbers_list = [abs(float(x)) for x in sequence.split()]
    return sequence_of_numbers_list


sequence_of_numbers = input()
print(absolute_value_list(sequence_of_numbers))
