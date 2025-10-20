def fibonacci_sequence(number: int) -> list:
    fib_list = ["1", "1", "2"]
    if number == 1:
        return ["1"]
    if number == 2:
        return ["1", "1"]
    if number == 3:
        return ["1", "1", "2"]
    while True:
        if len(fib_list) == number:
            break
        x = int(fib_list[-1])
        y = int(fib_list[-2])
        z = int(fib_list[-3])
        total = str(x + y + z)
        fib_list.append(total)
    return fib_list


n = int(input())
fibonacci_list = fibonacci_sequence(n)
print(" ".join(fibonacci_list))
