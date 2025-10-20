old_version = input().split(".")
version_as_string = ""
new_version_list = []

for i in old_version:
    version_as_string += i

version_as_digit = int(version_as_string)
new_version = version_as_digit + 1
new_version_as_string = str(new_version)

for i in new_version_as_string:
    new_version_list.append(i)
    new_version_list.append(".")

new_version_list.pop(-1)

print("".join(new_version_list))
