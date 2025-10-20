sequence_of_numbers = input().split(", ")
numbers = [int(x) for x in sequence_of_numbers]

max_number = max(numbers)
group_boundary = 10

while numbers:
    current_group = [num for num in numbers if num <= group_boundary]
    numbers = [num for num in numbers if num > group_boundary]
    print(f"Group of {group_boundary}'s: {current_group}")
    group_boundary += 10
