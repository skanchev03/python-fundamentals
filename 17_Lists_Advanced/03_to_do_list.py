to_do_list = []
final_list = []

while True:
    to_do_note = input()
    if to_do_note == "End":
        break
    to_do_list.append(to_do_note)

to_do_list_sorted = sorted(to_do_list, key=lambda x: int(x.split("-")[0]))

for note in to_do_list_sorted:
    final_list.append(note.split("-")[1])

print(final_list)
