cards_string = input()
shuffles_count = int(input())

cards_list = cards_string.split()
deck_split = len(cards_list) // 2

for number_of_shuffles in range(shuffles_count):
    first_half = []
    second_half = []
    shuffled_cards_list = []

    for first_half_cards in range(deck_split):
        first_half.append(cards_list[first_half_cards])

    for second_half_cards in range(deck_split, len(cards_list)):
        second_half.append((cards_list[second_half_cards]))

    for cards in range(deck_split):
        shuffled_cards_list.append(first_half[cards])
        shuffled_cards_list.append(second_half[cards])

    cards_list, shuffled_cards_list = shuffled_cards_list, cards_list

print(cards_list)
