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
        for j in range(0, i - 1):
            if list[j] > list[j+1]:
                swap(list, j, j+1)
    return list

print(bubble_sort([7,3, 5, 1, 9]))
