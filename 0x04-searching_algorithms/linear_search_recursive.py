def linear_search(list, value, i):
    if i >= len(list):
        return -1
    if list[i] == value:
        return i
    i += 1
    return linear_search(list, value, i)

print(linear_search([10, 1, 13, 4, 6], 13, 0))
print(linear_search([10, 1, 13, 4, 6], 23, 0))