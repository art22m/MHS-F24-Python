from fib import fib
import time
import multiprocessing

if __name__ == '__main__':
    start = time.time()
    jobs = []
    for i in range(10):
        thread = multiprocessing.Process(target=fib, args=(123456,))
        jobs.append(thread)
    for j in jobs:
        j.start()
    for j in jobs:
        j.join()
    print(f"Fib process time: {time.time() - start:.4f}s")
