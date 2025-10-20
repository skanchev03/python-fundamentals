some_list = input().split()
even_list = [word for word in some_list if len(word) % 2 == 0]
print("\n".join(even_list))
