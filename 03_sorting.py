import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for i in range(n - i - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]


def bubble_sort_adaptive(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break  # No swaps means the array is sorted already


if __name__ == "__main__":
    random.seed(42)  # For reproducibility

    sample_list = [random.randint(1, 100) for _ in range(random.randint(10, 20))]
    bubble_sort(sample_list)
    print("Bubble Sorted array:", sample_list)