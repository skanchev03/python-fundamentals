def calculate_time(time:list[int]) -> float:
    final_time = 0
    for number in time:
        if number != 0:
            final_time += number
        else:
            final_time *= 0.8
    return final_time


sequence_of_numbers = [int(x) for x in input().split()]
middle = len(sequence_of_numbers) // 2
left = sequence_of_numbers[0:middle]
right = sequence_of_numbers[-1:middle:-1]

left_time = calculate_time(left)
right_time = calculate_time(right)

if left_time < right_time:
    print(f"The winner is left with total time: {left_time:.1f}")
else:
    print(f"The winner is right with total time: {right_time:.1f}")
