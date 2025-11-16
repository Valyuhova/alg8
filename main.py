import random
import time
import sys

sys.setrecursionlimit(20000)


def partition(arr, p, r, stats):
    x = arr[r]
    stats["asg"] += 1

    i = p - 1
    stats["asg"] += 1

    for j in range(p, r):
        stats["cmp"] += 1
        if arr[j] <= x:
            i += 1
            stats["asg"] += 1

            arr[i], arr[j] = arr[j], arr[i]
            stats["asg"] += 3

    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    stats["asg"] += 3

    return i + 1


def quicksort(arr, p, r, stats):
    if p < r:
        q = partition(arr, p, r, stats)
        stats["asg"] += 1

        quicksort(arr, p, q - 1, stats)
        quicksort(arr, q + 1, r, stats)


def quicksort_wrapper(arr):
    stats = {"cmp": 0, "asg": 0}
    if len(arr) > 0:
        quicksort(arr, 0, len(arr) - 1, stats)
    return stats["cmp"], stats["asg"]


def generate_array(n, mode):
    if mode == "random":
        return [random.randint(0, 100000) for _ in range(n)]
    elif mode == "ascending":
        return list(range(n))
    elif mode == "descending":
        return list(range(n, 0, -1))
    else:
        return []


def main():
    sizes = [10, 100, 1000, 5000, 10000]
    modes = ["random", "ascending", "descending"]

    results = []

    for n in sizes:
        for mode in modes:
            arr = generate_array(n, mode)
            data = arr[:]

            start_time = time.perf_counter()
            cmp_count, asg_count = quicksort_wrapper(data)
            end_time = time.perf_counter()

            elapsed = end_time - start_time

            results.append({
                "n": n,
                "mode": mode,
                "time": elapsed,
                "cmp": cmp_count,
                "asg": asg_count
            })


    print("РЕЗУЛЬТАТИ ДОСЛІДЖЕННЯ АЛГОРИТМУ ШВИДКОГО СОРТУВАННЯ\n")
    print(f"{'n':>7} {'тип послідовності':>20} {'час, с':>12} {'порівняння':>15} {'присвоєння':>15}")
    print("-" * 75)

    for res in results:
        mode_name = {
            "random": "випадкова",
            "ascending": "зростаюча",
            "descending": "спадна"
        }[res["mode"]]

        print(f"{res['n']:7d} {mode_name:>20} {res['time']:12.6f} {res['cmp']:15d} {res['asg']:15d}")


if __name__ == "__main__":
    main()