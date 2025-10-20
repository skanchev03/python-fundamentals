a = int(input())
b = int(input())
temp = 0

print("Before:")
print(f"a = {a}")
print(f"b = {b}")

temp = a
a = b
b = temp

print("After:")
print(f"a = {a}")
print(f"b = {b}")
