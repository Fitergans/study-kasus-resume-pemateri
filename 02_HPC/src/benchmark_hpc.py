from multiprocessing import Pool, cpu_count
from time import perf_counter
import math
import os

def hitung_blok(args):
    start, end = args
    total = 0.0
    for i in range(start, end):
        total += math.sqrt(i) % 17
    return total

def main():
    n = 1_000_000
    workers = min(cpu_count(), 4)
    blok = (n + workers - 1) // workers
    ranges = [(i, min(i + blok, n)) for i in range(0, n, blok)]

    t0 = perf_counter()
    serial = sum(hitung_blok(r) for r in ranges)
    serial_time = perf_counter() - t0

    t0 = perf_counter()
    with Pool(processes=workers) as pool:
        parallel = sum(pool.map(hitung_blok, ranges))
    parallel_time = perf_counter() - t0

    print(f"Ukuran tugas: {n:,}; worker: {workers}; CPU tersedia: {cpu_count()}")
    print(f"Hasil serial   : {serial:.6f} | waktu: {serial_time:.3f} detik")
    print(f"Hasil paralel  : {parallel:.6f} | waktu: {parallel_time:.3f} detik")
    print(f"Speedup        : {serial_time / parallel_time:.2f}x")
    print("Kesamaan hasil :", math.isclose(serial, parallel, rel_tol=1e-10))
    print("Catatan: hasil benchmark bergantung pada CPU, OS, dan beban sistem.")

if __name__ == "__main__":
    main()
