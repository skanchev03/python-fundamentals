def exchange(given_list: list[int], given_index: int):
    given_list = given_list[given_index + 1:] + given_list[:given_index + 1]
    return given_list


def get_max_and_min(given_list: list[int], keyword: str, doing: str):
    if keyword == "even":
        max_min_list = [x for x in given_list if x % 2 == 0]
    else:
        max_min_list = [x for x in given_list if x % 2 != 0]
    if not max_min_list:
        return "No matches"
    reversed_initial_list = given_list[::-1]
    if doing == "max":
        max_number = max(max_min_list)
        max_number_index = len(given_list) - reversed_initial_list.index(max_number) - 1
        return max_number_index
    min_number = min(max_min_list)
    min_number_index = len(given_list) - reversed_initial_list.index(min_number) - 1
    return min_number_index


def get_first_and_last(given_list: list[int], amount: int, keyword: str, doing: str):
    if amount > len(given_list):
        return "Invalid count"
    if keyword == "even":
        first_last_list = [x for x in given_list if x % 2 == 0]
    else:
        first_last_list = [x for x in given_list if x % 2 != 0]
    if not first_last_list:
        return "[]"
    if amount > len(first_last_list):
        return first_last_list
    final_list = list()
    if doing == "first":
        for i in range(amount):
            final_list.append(first_last_list[i])
        return final_list
    for i in range(1, amount + 1):
        final_list.append(first_last_list[-i])
    return final_list[::-1]


initial_list = [int(x) for x in input().split()]

while True:
    command = input()

    if command == "end":
        break

    command_parts = command.split()
    action = command_parts[0]

    if action == "exchange":
        index = int(command_parts[1])
        if index < 0 or index >= len(initial_list):
            print("Invalid index")
        else:
            initial_list = exchange(initial_list, index)

    elif action == "max" or action == "min":
        even_or_odd = command_parts[1]
        print(get_max_and_min(initial_list, even_or_odd, action))

    elif action == "first" or action == "last":
        count = int(command_parts[1])
        even_or_odd = command_parts[2]
        print(get_first_and_last(initial_list, count, even_or_odd, action))

print(initial_list)
