n = int(input())
prime = True

for divisor in range(2, n):
    if n % divisor == 0:
        prime = False
        break

print(prime)
