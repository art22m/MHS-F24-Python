def fib(n: int) -> int:
    a, b = 1, 1
    for i in range(3, n + 1):
        a, b = b, a + b
    return b
