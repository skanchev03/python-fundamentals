number = int(input())

if number == 100:
    print("100% Complete!")
    print("[%%%%%%%%%%]")
if  10 <= number <= 90:
    percent_string = "%" * (number // 10)
    dots_string = "." * ((100 - number) // 10)
    print(f"{number}% [{percent_string}{dots_string}]")
    print("Still loading...")
