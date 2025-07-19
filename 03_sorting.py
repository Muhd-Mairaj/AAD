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


def counting_sort(arr):
    k = max(arr)
    count = [0] * (k+1)

    # count the frequency of each element
    for num in arr:
        count[num] += 1

    index = 0
    for i in range(1, k+1):
        # place the element based on its frequency
        # e.g. if count[3] = 2, then 3 will be placed twice in the sorted array
        while count[i] > 0:
            arr[index] = i
            index += 1
            count[i] -= 1


def counting_sort_by_digit(arr, exp):
    count = [0] * 10  # For digits 0-9
    output = [0] * len(arr)

    # count occurrences of each digit at `exp` position
    # e.g. if exp = 100, we count the tens place
    # (2157 // 100) = 21, (21 % 10) = 1
    for num in arr:
        index = (num // exp) % 10
        count[index] += 1

    # compute the running sum
    for i in range(1, 10):
        count[i] += count[i - 1]

    # build the output array (in reverse)
    for i in reversed(range(len(arr))):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    # copy the output array back to the original array
    for i in range(len(arr)):
        arr[i] = output[i]

    
def radix_sort(arr):
    # find number of digits in the maximum number
    max_num = max(arr)
    digits = len(str(max_num))

    for i in range(0, digits):
        exp = 10 ** i  # Exponent for the current digit
        counting_sort_by_digit(arr, exp)
        

if __name__ == "__main__":
    random.seed(42)  # For reproducibility

    sample_list = [random.randint(1, 100) for _ in range(random.randint(10, 20))]
    print("Original array:", sample_list)

    radix_sort(sample_list)
    print("Sorted array:", sample_list)