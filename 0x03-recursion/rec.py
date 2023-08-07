def print_array_element(list, i):
    list_length = len(list)
    print(list[i])
    i += 1
    if i >= list_length:
        return
    print_array_element(list, i)

print_array_element([1, 2, 3, 4, 5], 0)