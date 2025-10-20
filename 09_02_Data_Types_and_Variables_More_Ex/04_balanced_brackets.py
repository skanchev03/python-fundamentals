number_of_lines = int(input())
balanced = True
counter = 0

for i in range(number_of_lines):
    string = input()

    if string == "(":
        counter += 1

    if string == ")":
        counter -= 1

    if counter == -1 or counter == 2:
        balanced = False

if balanced:
    print("BALANCED")
else:
    print("UNBALANCED")
