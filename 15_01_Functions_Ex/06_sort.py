def sorted_numbers_list(numbers_list: list) -> list:
    return sorted(numbers_list)


sequence_of_numbers = list(map(int, input().split()))
print(sorted_numbers_list(sequence_of_numbers))
