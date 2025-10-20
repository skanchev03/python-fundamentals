def data_types(some_command: str, something: str) -> str:
    if some_command == "int":
        return f"{int(something) * 2}"
    if some_command == "real":
        return f"{float(something) * 1.5:.2f}"
    if some_command == "string":
        return f"${something}$"


command = input()
commanded_variable = input()
print(data_types(command, commanded_variable))
