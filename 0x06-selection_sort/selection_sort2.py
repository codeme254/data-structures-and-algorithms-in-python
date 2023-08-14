"""The selection sort algorithm"""

def swap_list_elements(list, index1:int, index2:int):
    """
    swaps two elements in a list
    """
    temp = list[index1]
    list[index1] = list[index2]
    list[index2] = temp

def selection_sort(list):
    """
    Performs the selection sort algorithm on a list
    """
    for i in range(0, len(list)):
        lowest = i
        for j in range(i+1, len(list)):
            if list[j] < list[lowest]:
                lowest = j
        swap_list_elements(list, i, lowest)
    return list

print(selection_sort([0, 2, 5, 1, 9]))
print(selection_sort([3, 2, 5, 1, 9]))
print(selection_sort([7,3, 5, 1, 9]))
print(selection_sort([12, 7, 18, 5, 11, 9, 6, 2, 3, 14]))
print(selection_sort([33, 25, 19, 29, 8, 36, 42, 17]))
print(selection_sort([64, 73, 55, 91, 88, 60, 82, 47]))
print(selection_sort([52, 15, 70, 39, 4, 63, 86, 28]))
print(selection_sort([44, 77, 69, 31, 23, 57, 95, 83]))
print(selection_sort(['banana', 'cherry', 'apple', 'kiwi', 'grape', 'orange', 'pear', 'watermelon']))
print(selection_sort(['strawberry', 'pineapple', 'orange', 'tangerine', 'watermelon', 'quince', 'raspberry']))
print(selection_sort(['cranberry', 'apricot', 'grapefruit', 'blueberry', 'dragonfruit', 'fig']))
print(selection_sort(['honeydew', 'cherry', 'date', 'kiwi', 'elderberry', 'grape', 'banana']))