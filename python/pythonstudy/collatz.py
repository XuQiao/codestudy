def collatz(n):
    print(n)
    if n % 2 == 1 and n > 1:
        collatz(3*n + 1)
    elif n % 2 == 0:
        collatz(n / 2)
