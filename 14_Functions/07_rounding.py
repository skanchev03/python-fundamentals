def rounded_numbers_list(sequence: str) -> list:
    sequence_of_numbers_list = [round(float(x)) for x in sequence.split()]
    return sequence_of_numbers_list


sequence_of_numbers = input()
print(rounded_numbers_list(sequence_of_numbers))
