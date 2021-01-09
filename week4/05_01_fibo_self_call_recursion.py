input = 20

# 재귀함수

def fibo_recursion(n):

    if n == 1 or n == 2:
        return 1

    return fibo_recursion(n - 1) + fibo_recursion(n - 2)


print(fibo_recursion(input))  # 6765

# 시간복잡도
# fibo(4)
# fibo(3) + fib0(2)
# fibo(2) + fibo(1) + 1 연산 3번

# fibo(5)
# fibo(4) + fibo(3)
# fibo(3) + fibo(2) + fibo(2) + fibo(1)
# fibo(2) + fibo(1) + fibo(2) + fibo(2) + fibo(1)

#>..