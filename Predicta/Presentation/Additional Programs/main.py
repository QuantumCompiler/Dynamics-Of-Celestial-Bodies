import time
import sys

def count_to(n: int, progress_every: int = 50_000_000) -> float:
    start = time.perf_counter()
    i = 0
    while i < n:
        i += 1
        if progress_every and (i % progress_every == 0):
            elapsed = time.perf_counter() - start
            print(f"Reached {i:,} / {n:,}  (elapsed: {elapsed:.2f}s)")
            sys.stdout.flush()
    end = time.perf_counter()
    return end - start

def main() -> None:
    n = 1_000_000_000
    print(f"Counting to {n:,}...")
    elapsed = count_to(n)
    print(f"Done. Elapsed time: {elapsed:.6f} seconds")

if __name__ == "__main__":
    main()