def swap(list, index1, index2):
    """
    swaps a two elements of a list in place
    """
    temp = list[index1]
    list[index1] = list[index2]
    list[index2] = temp

def bubble_sort(list):
    """
    Performs the bubble sort algorithm on a list and sorts the list in ascending order

    list: the list of elements that should be sorted
    """
    for i in range(len(list)-1, -1, -1):
        for j in range(0, i):
            if list[j] > list[j+1]:
                swap(list, j, j+1)
    return list

print(bubble_sort([5, 4, 3, 2, 1]))
print(bubble_sort([12, 7, 18, 5, 11, 9, 6, 2, 3, 14]))
print(bubble_sort([33, 25, 19, 29, 8, 36, 42, 17]))
print(bubble_sort([64, 73, 55, 91, 88, 60, 82, 47]))
print(bubble_sort([52, 15, 70, 39, 4, 63, 86, 28]))
print(bubble_sort([44, 77, 69, 31, 23, 57, 95, 83]))
print(bubble_sort(['banana', 'cherry', 'apple', 'kiwi', 'grape', 'orange', 'pear', 'watermelon']))
print(bubble_sort(['strawberry', 'pineapple', 'orange', 'tangerine', 'watermelon', 'quince', 'raspberry']))
print(bubble_sort(['cranberry', 'apricot', 'grapefruit', 'blueberry', 'dragonfruit', 'fig']))
print(bubble_sort(['honeydew', 'cherry', 'date', 'kiwi', 'elderberry', 'grape', 'banana']))

