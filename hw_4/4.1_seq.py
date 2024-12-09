from fib import fib
import time

if __name__ == '__main__':
    start = time.time()
    for _ in range(10):
        fib(123456)
    print(f"Fib seq time: {time.time() - start:.4f}s")