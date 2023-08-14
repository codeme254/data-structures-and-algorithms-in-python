"""insertion sort algorithm"""
def swap_list_elements(list, index1:int, index2:int):
    """
    swaps two elements in a list
    """
    temp = list[index1]
    list[index1] = list[index2]
    list[index2] = temp

def insertion_sort(list):
    """
    Performs the insertion sort algorithm on a list
    """
    if len(list) <= 1:
        return list
    
    i = 1
    while i < len(list):
        j = i
        while j > 0:
            if list[j] < list[j-1]:
                swap_list_elements(list, j, j-1)
                j -= 1
            else:
                break
        i += 1
    return list

print(insertion_sort([0, 2, 5, 1, 9]))
print(insertion_sort([3, 2, 5, 1, 9]))
print(insertion_sort([7,3, 5, 1, 9]))
print(insertion_sort([12, 7, 18, 5, 11, 9, 6, 2, 3, 14]))
print(insertion_sort([33, 25, 19, 29, 8, 36, 42, 17]))
print(insertion_sort([64, 73, 55, 91, 88, 60, 82, 47]))
print(insertion_sort([52, 15, 70, 39, 4, 63, 86, 28]))
print(insertion_sort([44, 77, 69, 31, 23, 57, 95, 83]))
print(insertion_sort(['banana', 'cherry', 'apple', 'kiwi', 'grape', 'orange', 'pear', 'watermelon']))
print(insertion_sort(['strawberry', 'pineapple', 'orange', 'tangerine', 'watermelon', 'quince', 'raspberry']))
print(insertion_sort(['cranberry', 'apricot', 'grapefruit', 'blueberry', 'dragonfruit', 'fig']))
print(insertion_sort(['honeydew', 'cherry', 'date', 'kiwi', 'elderberry', 'grape', 'banana']))
