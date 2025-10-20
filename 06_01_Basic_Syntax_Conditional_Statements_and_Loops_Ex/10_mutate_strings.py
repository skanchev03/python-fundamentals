string_one = input()
string_two = input()
new_string = ""

for i in range(len(string_one)):
    new_string = string_two[0:i+1:] + string_one[i+1::]

    if string_one[i] != string_two[i]:
        print(new_string)
