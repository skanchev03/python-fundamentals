def password_validator(some_password: str):
    valid_password = True
    if len(some_password) < 6 or len(some_password) > 10:
        valid_password = False
        print("Password must be between 6 and 10 characters")
    if not some_password.isalnum():
        valid_password = False
        print("Password must consist only of letters and digits")
    digit_counter = 0
    for i in some_password:
        if i.isdigit():
            digit_counter += 1
    if digit_counter < 2:
        valid_password = False
        print("Password must have at least 2 digits")
    if valid_password:
        print("Password is valid")



password = input()
password_validator(password)
