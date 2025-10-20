n = int(input())
positive_list = []
negative_list = []
positive_count = 0
negative_sum = 0

for _ in range(n):
    number = int(input())

    if number >= 0:
        positive_list.append(number)
        positive_count += 1
    else:
        negative_list.append(number)
        negative_sum += number

print(positive_list)
print(negative_list)
print(f"Count of positives: {positive_count}")
print(f"Sum of negatives: {negative_sum}")
