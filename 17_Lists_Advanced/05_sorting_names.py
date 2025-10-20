names_list = input().split(", ")
names_list_sorted = sorted(names_list, key=lambda name: (-len(name), name))
print(names_list_sorted)
