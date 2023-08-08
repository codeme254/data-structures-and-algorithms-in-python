from math import floor
def binary_search(list, value):
    start = 0
    end = len(list) - 1
    middle = floor((start + end) / 2)

    while (list[middle] != value and start <= end):
        if value < list[middle]:
            end = middle - 1
        else:
            start = middle + 1
        middle = floor((start + end) / 2)

    if list[middle] == value:
        return middle
    return -1

print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 8))
print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 11))
print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 20))
print(binary_search([1, 2, 3, 4], 2.3))
print(binary_search([1, 2, 3, 4], 1.3))
print(binary_search([1], 1))
