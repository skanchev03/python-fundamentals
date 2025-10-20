numbers_string = input()
n = int(input())
numbers_list = [int(num) for num in numbers_string.split()]
sorted_numbers_list = sorted(numbers_list, reverse=True)
removed_numbers = []

for _ in range(n):
    removed_numbers.append(sorted_numbers_list[-1])
    sorted_numbers_list.remove(sorted_numbers_list[-1])

for number in removed_numbers:
    if number in numbers_list:
        numbers_list.remove(number)

for i in range(len(numbers_list)):
    if i != len(numbers_list) - 1:
        print(numbers_list[i],end=", ")
    else:
        print(numbers_list[i])
