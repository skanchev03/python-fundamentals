potential_palindromes = input().split()
special_palindrome = input()
palindromes_list = []
special_palindrome_counter = 0

for palindrome in potential_palindromes:
    if palindrome == palindrome[::-1]:
        palindromes_list.append(palindrome)

for special in palindromes_list:
    if special == special_palindrome:
        special_palindrome_counter += 1

print(palindromes_list)
print(f"Found palindrome {special_palindrome_counter} times")
