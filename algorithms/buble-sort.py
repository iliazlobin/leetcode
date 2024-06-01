def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

numbers = [5, 2, 3, 1, 4]
bubble_sort(numbers)
print(numbers)  # Output: [1, 2, 3, 4, 5]
