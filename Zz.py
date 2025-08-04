import time
from multiprocessing import Pool, cpu_count

def calc_pi_range(args):
    start, end = args
    s = 0
    for k in range(start, end):
        s += ((-1) ** k) / (2 * k + 1)
    return s

def cpu_benchmark_multi(n=10**8):
    print(f"多进程并行计算π的前{n}项（CPU多核性能测试）")
    num_workers = cpu_count()
    print(f"检测到 CPU 核心数: {num_workers}")

    chunk = n // num_workers
    ranges = [(i * chunk, (i + 1) * chunk if i < num_workers - 1 else n) for i in range(num_workers)]
    print(ranges)
    start_time = time.time()
    with Pool(num_workers) as pool:
        results = pool.map(calc_pi_range, ranges)
    pi = sum(results) * 4
    elapsed = time.time() - start_time

    print(f"计算耗时: {elapsed:.2f} 秒")
    print(f"结果π ≈ {pi}")

# 这里是关键
if __name__ == '__main__':
    cpu_benchmark_multi()

