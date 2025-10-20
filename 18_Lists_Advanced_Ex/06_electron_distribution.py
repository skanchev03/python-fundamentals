electrons = int(input())
electrons_list = []

while True:
    electrons_needed = 2 * (len(electrons_list) + 1)**2
    if electrons_needed >= electrons:
        electrons_list.append(electrons)
        break
    electrons_list.append(electrons_needed)
    electrons -= electrons_needed

print(electrons_list)
