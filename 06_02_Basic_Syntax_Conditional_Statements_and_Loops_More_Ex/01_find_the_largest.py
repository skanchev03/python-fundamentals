number = int(input())
digits_list = list(str(number))

for i in range(len(digits_list)):
    for j in range(0, len(digits_list) - i - 1):
        if digits_list[j] < digits_list[j + 1]:
            digits_list[j], digits_list[j+1] = digits_list[j+1], digits_list[j]

for i in range(len(digits_list)):
    print(digits_list[i],end="")
