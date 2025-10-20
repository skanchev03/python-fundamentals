n = int(input())
special_word = input()
word_list = []
special_word_list = []

for _ in range(n):
    word = input()

    word_list.append(word)

    if special_word in word:
        special_word_list.append(word)

print(word_list)
print(special_word_list)
