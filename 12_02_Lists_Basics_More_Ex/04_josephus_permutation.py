number_sequence = input().split()
k = int(input())
final_list = list()
index = 0

while number_sequence:
    index = (index + k - 1) % len(number_sequence)
    final_list.append(number_sequence.pop(index))

print("[" + ",".join(x for x in final_list) + "]")
