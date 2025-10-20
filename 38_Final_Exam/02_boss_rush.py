import re

number_of_lines = int(input())
pattern = re.compile(r"^\|([A-Z]{4,})\|:#([A-Za-z]+ [A-Za-z]+)#$")

for _ in range(number_of_lines):
    line = input()
    valid = pattern.match(line)

    if valid:
        boss_name = valid.group(1)
        title = valid.group(2)
        print(f"{boss_name}, The {title}")
        print(f">> Strength: {len(boss_name)}")
        print(f">> Armor: {len(title)}")
    else:
        print("Access denied!")
