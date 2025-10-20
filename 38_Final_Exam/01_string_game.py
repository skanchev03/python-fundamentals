def change(replace, replacement, string_containing):
    while replace in string_containing:
        index = string_containing.index(replace)
        string_containing[index] = replacement
    return string_containing


def includes(some_substring, some_string):
    string_to_check = "".join(some_string)
    if some_substring in string_to_check:
        return True
    return False


def end(some_substring, some_string):
    string_to_check = "".join(some_string)
    return string_to_check.endswith(some_substring)


def uppercase(string_to_upper):
    string_to_up = "".join(string_to_upper)
    string_up = string_to_up.upper()
    list_to_return = [x for x in string_up]
    return list_to_return


def find_index(some_char, some_list):
    return some_list.index(some_char)


def cut(start, amount, some_list):
    new_list = []
    for _ in range(amount):
        new_list.append(some_list.pop(start))
    return new_list


initial_string = input()
initial_string_as_list = [x for x in initial_string]

while True:
    commands = input().split()
    command = commands[0]

    if command == "Done":
        break

    if command == "Change":
        replace_this = commands[1]
        with_that = commands[2]
        initial_string_as_list = change(replace_this, with_that, initial_string_as_list)
        print("".join(initial_string_as_list))

    if command == "Includes":
        substring = commands[1]
        print(includes(substring, initial_string_as_list))

    if command == "End":
        substring = commands[1]
        print(end(substring, initial_string_as_list))

    if command == "Uppercase":
        initial_string_as_list = uppercase(initial_string_as_list)
        print("".join(initial_string_as_list))

    if command == "FindIndex":
        character = commands[1]
        print(find_index(character, initial_string_as_list))

    if command == "Cut":
        start_index = int(commands[1])
        count = int(commands[2])
        initial_string_as_list = cut(start_index, count, initial_string_as_list)
        print("".join(initial_string_as_list))
