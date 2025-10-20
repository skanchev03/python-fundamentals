def multiplication_sign(x: int, y: int, z: int):
    if x == 0 or y == 0 or z == 0:
        return "zero"
    if x > 0 and y > 0 and z > 0 or x > 0 > y and z < 0 or x < 0 < y and z < 0 or x < 0 < z and y < 0:
        return "positive"
    if x < 0 and y < 0 and z < 0 or x > 0 > z and y > 0 or x > 0 > y and z < 0 or x < 0 < y and z > 0:
        return "negative"

first = int(input())
second = int(input())
third = int(input())

print(multiplication_sign(first, second, third))
