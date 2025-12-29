import time

def find(arr, q):
    """
    Linear search for element q in array arr.

    Code Reading: What does it do?
    - Iterates through the array from index 0
    - Compares each element to the query q
    - Returns the index if found
    - Returns -1 if not found

    Execution Time: How long does it take?
    - Depends on the size of the array (n)
    - Depends on WHERE the query is located!

    Asymptotics:
    - Best case:  O(1)   - found at first position
    - Worst case: O(n)   - found at last position, or not found
    - Average case: O(n) - on average, check n/2 elements
    """
    for i in range(len(arr)):
        if arr[i] == q:
            return i
    return -1


def demonstrate_running_time():
    """Demonstrate how running time depends on query location."""
    n = 1_000_000
    arr = list(range(n))

    # Best case: element at the beginning
    start = time.perf_counter()
    result = find(arr, 0)
    best_time = time.perf_counter() - start
    print(f"Best case (q=0, found at index 0):      {best_time:.6f} sec")

    # Average case: element in the middle
    start = time.perf_counter()
    result = find(arr, n // 2)
    avg_time = time.perf_counter() - start
    print(f"Average case (q={n//2}, found at middle): {avg_time:.6f} sec")

    # Worst case: element at the end
    start = time.perf_counter()
    result = find(arr, n - 1)
    worst_time = time.perf_counter() - start
    print(f"Worst case (q={n-1}, found at end):   {worst_time:.6f} sec")

    # Worst case: element not found
    start = time.perf_counter()
    result = find(arr, -1)
    not_found_time = time.perf_counter() - start
    print(f"Worst case (q=-1, not found):           {not_found_time:.6f} sec")


def demonstrate_linear_growth():
    """Demonstrate O(n) worst-case growth."""
    print("\nWorst case (not found) for increasing n:")
    print("n\t\ttime (sec)\tratio")
    print("-" * 45)

    sizes = [100_000, 200_000, 400_000, 800_000, 1_600_000]
    prev_time = None

    for n in sizes:
        arr = list(range(n))

        start = time.perf_counter()
        result = find(arr, -1)  # not found = worst case
        elapsed = time.perf_counter() - start

        ratio = f"{elapsed / prev_time:.2f}" if prev_time else "-"
        print(f"{n:,}\t\t{elapsed:.6f}\t{ratio}")
        prev_time = elapsed


if __name__ == "__main__":
    # Basic usage
    test = [32, 11, 73, 21, 29, 86, 81, 92, 57, 61, 64, 15, 79, 44, 7, 45]
    print(f"arr = {test}")
    print(f"find(arr, 29) = {find(test, 29)}")
    print(f"find(arr, 99) = {find(test, 99)}")
    print()

    # Demonstrate dependence on query location
    print("Demonstrating how running time depends on query value:\n")
    demonstrate_running_time()

    # Demonstrate linear growth
    demonstrate_linear_growth()
