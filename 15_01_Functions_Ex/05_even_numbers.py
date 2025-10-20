def even_numbers(list_of_numbers: list) -> list:
    even_numbers_list = list(filter(lambda x: x % 2 == 0, list_of_numbers))
    return even_numbers_list

numbers_list = list(map(int, input().split()))
print(even_numbers(numbers_list))
