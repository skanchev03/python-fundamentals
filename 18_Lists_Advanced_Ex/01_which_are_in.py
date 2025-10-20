substrings = input().split(", ")
strings = input().split(", ")
contained = []

for substring in substrings:
    for string in strings:
        if substring in string:
            contained.append(substring)
            break


print(contained)
