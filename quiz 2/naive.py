import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

if __name__ == "__main__":
    random.seed(40)
    arr = [random.randint(0, 100) for _ in range(50)]
    print("Original Array:", arr)
    sorted_arr = bubble_sort(arr)
    print("Sorted Array:", sorted_arr)