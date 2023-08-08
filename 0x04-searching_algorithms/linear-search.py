def linear_search(list, value):
    for i in range(0, len(list)):
        if list[i] == value:
            return i
    return -1

print(linear_search([10, 1, 13, 4, 6], 13))
print(linear_search([10, 1, 13, 4, 6], 23))