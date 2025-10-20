def sum_numbers(first_number: int, second_number: int) -> int:
    return first_number + second_number


def subtract(first_and_second_summed: int, third_number: int) -> int:
    return first_and_second_summed - third_number

first_num = int(input())
second_num = int(input())
third_num = int(input())

first_and_second_sum = sum_numbers(first_num, second_num)
print(subtract(first_and_second_sum, third_num))
