string = input()
upper_list = []


for i, c in enumerate(string):
    if c.isupper():
        upper_list.append(i)

print(upper_list)
