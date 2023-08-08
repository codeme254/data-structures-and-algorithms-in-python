from math import ceil
def binary_search(list, value):
    left = 0
    right = len(list) - 1

    while left <= right:
        middle = ceil((left + right)/2)
        if (middle == left or middle == right) and list[middle] != value:
            return -1
        if list[middle] == value:
            return middle
        elif list[middle] > value:
            right = middle
        elif list[middle] < value:
            left = middle
    return -1

print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 8))
print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 11))
print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 20))
print(binary_search([1, 2, 3, 4], 2.3))
print(binary_search([1, 2, 3, 4], 1.3))
print(binary_search([1], 1))