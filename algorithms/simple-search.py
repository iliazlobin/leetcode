def linear_search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i  # Return the index of the target
    return -1  # Return -1 if the target is not found

numbers = [1, 2, 3, 4, 5]
print(linear_search(numbers, 3))  # Output: 2
print(linear_search(numbers, 6))  # Output: -1
