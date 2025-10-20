def factorial_calculator(some_number: int) -> int:
    factorial = 1
    for i in range(1, some_number + 1):
        factorial *= i
    return factorial


first_num = int(input())
second_num = int(input())

first_factorial = factorial_calculator(first_num)
second_factorial = factorial_calculator(second_num)
print(f"{first_factorial / second_factorial:.2f}")
