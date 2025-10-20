first_index = int(input())
last_index = int(input())

for i in range(first_index, last_index + 1):
    if i != last_index:
        print(chr(i), end=" ")
    else:
        print(chr(i))
