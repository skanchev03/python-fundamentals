number = int(input())

for numbers in range(1, number + 1):
    sum_digits = 0
    str_numbers = str(numbers)
    for digits in str_numbers:
        sum_digits += int(digits)
    if sum_digits == 5 or sum_digits == 7 or sum_digits == 11:
        print(f"{numbers} -> True")
    else:
        print(f"{numbers} -> False")
