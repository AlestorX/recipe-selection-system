import time

from sorting import LoopSort, RecursiveSort


def run_performance_analysis(recipes):
    """Compare the speed of LoopSort and RecursiveSort."""
    if not recipes:
        print("There are no recipes to test.")
        return

    loop_sorter = LoopSort()
    recursive_sorter = RecursiveSort()

    # Time the loop sort (insertion sort) on a copy of the list.
    start = time.perf_counter()
    loop_sorter.sort(list(recipes), "price")
    loop_time = time.perf_counter() - start

    # Time the recursive sort (merge sort) on a copy of the list.
    start = time.perf_counter()
    recursive_sorter.sort(list(recipes), "price")
    recursive_time = time.perf_counter() - start

    print("\nLoop sort time:", "{:.8f}".format(loop_time))
    print("Recursive sort time:", "{:.8f}".format(recursive_time))
    print("Insertion sort: O(n^2)")
    print("Merge sort: O(n log n)")
