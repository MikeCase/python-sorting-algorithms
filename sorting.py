from selsort import SortAlgos
from helper_decorators import MyDecorators
import random

if __name__ == "__main__":
    unsorted_list = random.sample(range(0,10_000), 10_000)
    large_unsorted_list = random.sample(range(0, 100_000), 100_000)
    # unxsorted_list = random.sample(range(10), 10)
    sortalgos = SortAlgos()
    # print(unsorted_list)
    print(f"Performing an Insertion sort on {len(unsorted_list)} elements")
    sortalgos.insertionSort(unsorted_list)

    unsorted_list = random.sample(range(0,10_000), 10_000)
    print(f"Performing default python sorting algorithm on {len(unsorted_list)} elements")
    sortalgos.py_default_sorting_algo(unsorted_list)

    unsorted_list = random.sample(range(0,10_000), 10_000)
    print(f'Performing a Selection sort on {len(unsorted_list)} elements')
    sortalgos.selectionSort(unsorted_list)

    unsorted_list = random.sample(range(0,10_000), 10_000)
    print(f'Performing a Bubble Sort on {len(unsorted_list)} elements')
    sortalgos.bubbleSort(unsorted_list)

    unsorted_list = random.sample(range(0,10_000), 10_000)
    print(f'Performing a Comb Sort on {len(unsorted_list)} elements')
    sortalgos.combSort(unsorted_list)

    unsorted_list = random.sample(range(0,10_000), 10_000)
    print(f'Performing a Merge Sort on {len(unsorted_list)} elements')
    ms = MyDecorators.timer(sortalgos.mergeSort, n=100)(unsorted_list)
    # sortalgos.mergeSort(unsorted_list)
    ms