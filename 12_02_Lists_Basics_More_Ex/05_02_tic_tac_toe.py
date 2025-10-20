first_line = input().split()
second_line = input().split()
third_line = input().split()
first_column = [first_line[0], second_line[0], third_line[0]]
second_column = [first_line[1], second_line[1], third_line[1]]
third_column = [first_line[2], second_line[2], third_line[2]]
first_diagonal = [first_line[0], second_line[1], third_line[2]]
second_diagonal = [first_line[2], second_line[1], third_line[0]]

lines = [
    first_line, second_line, third_line,
    first_column, second_column, third_column,
    first_diagonal, second_diagonal
]

winner = False

for line in lines:
    if len(set(line)) == 1 and line[0] != "0":
        if line[0] == "1":
            print("First player won")
            winner = True
            break
        else:
            print("Second player won")
            winner = True
            break

if not winner:
    print("Draw!")
