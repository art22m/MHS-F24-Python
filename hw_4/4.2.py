import math, time
from multiprocessing import cpu_count
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def worker(s, f, a, step):
    from_v, to_v = s
    res = 0
    print(f"start processing from {from_v} to {to_v} \t at {time.time()}")
    for i in range(from_v, to_v):
        res += f(a + i * step) * step
    print(f"finish processing from {from_v} to {to_v} \t at {time.time()}")
    return res


def integrate(f, a, b, *, n_jobs=1, n_iter=10000000, pool=None):
    step = (b - a) / n_iter
    ranges = [
        (i * (n_iter // n_jobs), (i + 1) * (n_iter // n_jobs) if i != n_jobs - 1 else n_iter)
        for i in range(n_jobs)
    ]
    with pool(max_workers=n_jobs) as executor:
        results = executor.map(worker, ranges, [f] * n_jobs, [a] * n_jobs, [step] * n_jobs)
    return sum(results)


def main():
    for n_jobs in range(1, cpu_count() * 2 + 1):
        for (pool, name) in [(ThreadPoolExecutor, "thread_pool"), (ProcessPoolExecutor, "process_pool")]:
            start = time.time()
            print(f">> starting {name} with n_jobs={n_jobs}")
            integrate(
                math.cos, 0, math.pi / 2,
                n_jobs=n_jobs,
                pool=pool,
            )
            print(f">> finished {name} with n_jobs={n_jobs}, duration={time.time() - start:.4f}s")
            # print(f"{name} with n_jobs={n_jobs} takes {time.time()}s")
        print("---")


if __name__ == "__main__":
    main()
