# Implementasi Merge Sort
def merge_sort(arr):
    # Analisis Kompleksitas:
    # Best Case: O(n log n) -> Semua elemen hampir seimbang di tiap pembagian (data teracak).
    # Worst Case: O(n log n) -> Sama seperti best case karena pembagian selalu dilakukan setengah.
    # Average Case: O(n log n) -> Struktur pembagian tetap logaritmik, sehingga konsisten.

    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Implementasi Quick Sort
def quick_sort(arr):
    # Analisis Kompleksitas:
    # Best Case: O(n log n) -> Pivot selalu membagi array menjadi dua bagian yang sama besar (data acak).
    # Worst Case: O(n^2) -> Pivot selalu elemen terbesar atau terkecil (data terurut naik/turun).
    # Average Case: O(n log n) -> Secara rata-rata, pembagian mendekati seimbang.

    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  
    left = [x for x in arr if x < pivot]  
    middle = [x for x in arr if x == pivot]  
    right = [x for x in arr if x > pivot] 

    return quick_sort(left) + middle + quick_sort(right)

def sort_array(arr, method="merge"):
    if method == "merge":
        merge_sort(arr) 
        return arr
    elif method == "quick":
        return quick_sort(arr) 
    else:
        raise ValueError("Metode tidak valid. Gunakan 'merge' atau 'quick'.")

# Input Data
X = [1, 5, 6, 4, 3, 3, 3, 7, 7, 7, 9, 0, 1, 1, 3, 2, 1, 3, 4, 5, 6, 7, 8, 9, 0]

# Eksekusi Program
print("Array Asli:", X)

# Sorting menggunakan Merge Sort
sorted_merge = sort_array(X.copy(), method="merge")
print("Hasil Merge Sort:", sorted_merge)

# Sorting menggunakan Quick Sort
sorted_quick = sort_array(X.copy(), method="quick")
print("Hasil Quick Sort:", sorted_quick)