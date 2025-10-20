from math import sqrt, floor

def center_point(first_x: float, first_y: float, second_x: float, second_y: float):
    closer_x, closer_y, farther_x, farther_y = 0, 0, 0, 0
    if (first_x ** 2 + first_y ** 2) <= (second_x ** 2 + second_y ** 2):
        closer_x, closer_y = first_x, first_y
        farther_x, farther_y = second_x, second_y
    else:
        closer_x, closer_y = second_x, second_y
        farther_x, farther_y = first_x, first_y

    return floor(closer_x), floor(closer_y), floor(farther_x), floor(farther_y)


def longer_line_finder(x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float):
    line_a = sqrt((x2-x1)**2+(y2-y1)**2)
    line_b = sqrt((x4-x3)**2+(y4-y3)**2)
    if line_a >= line_b:
        close_x, close_y, far_x, far_y = center_point(x1, y1, x2, y2)
    else:
        close_x, close_y, far_x, far_y = center_point(x3, y3, x4, y4)
    return f"({close_x}, {close_y})({far_x}, {far_y})"

x_one = float(input())
y_one = float(input())
x_two = float(input())
y_two = float(input())
x_three = float(input())
y_three = float(input())
x_four = float(input())
y_four = float(input())

print(longer_line_finder(x_one, y_one, x_two, y_two, x_three, y_three, x_four, y_four))
