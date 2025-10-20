numbers_list = input().split(", ")
index_list = []

for index, number in enumerate(numbers_list):
    if int(number) % 2 == 0:
        index_list.append(index)

print(index_list)
