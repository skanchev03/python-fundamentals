string = input()
string = string.lower()

words_list = ["sand", "water", "fish", "sun"]
count_list = []

for word in words_list:
    count_list.append(string.count(word))

print(sum(count_list))
