def smallest_of_three_numbers(first_number: int, second_number: int, third_number: int) -> int:
    return min(first_number, second_number, third_number)

first_num = int(input())
second_num = int(input())
third_num = int(input())

print(smallest_of_three_numbers(first_num, second_num, third_num))
