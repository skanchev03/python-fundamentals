def calculator(operator: str, first_int: int, second_int: int):
    if operator == "multiply":
        return  first_int * second_int
    if operator == "divide":
        return first_int // second_int
    if operator == "add":
        return first_int + second_int
    if operator == "subtract":
        return first_int - second_int


operator_as_string = input()
integer_one = int(input())
integer_two = int(input())

print(calculator(operator_as_string, integer_one, integer_two))
