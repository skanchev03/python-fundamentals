from math import floor

def center_point(first_x: float, first_y: float, second_x: float, second_y: float) -> str:
    x, y = 0, 0
    if (first_x ** 2 + first_y ** 2) <= (second_x ** 2 + second_y ** 2):
        x, y = first_x, first_y
    else:
        x, y = second_x, second_y

    return f"({floor(x)}, {floor(y)})"


x_one = float(input())
y_one = float(input())
x_two = float(input())
y_two = float(input())

print(center_point(x_one, y_one, x_two, y_two))
