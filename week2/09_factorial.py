# Factorial(N) = N * Factorial(N-1) .. 반복
# factorial(1) = 1

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)


print(factorial(5))