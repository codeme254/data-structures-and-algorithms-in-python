# Insertion sort
- Builds up the sort by gradually creating a larger left half which is always sorted

- [```5```, 3, 4, 1, 2] - 5 has been inserted into a sorted position
- [```3, 5```, 4, 1, 2] - 3 has been inserted into a sorted position, now 3 and 5 are sorted
- [```3, 4, 5```, 1, 2] - 4 has been inserted into a sorted position, so 3, 4 and 5 are sorted.
- [```1, 3, 4, 5```, 2] - 1 has been inserted into a sorted position, so 1, 3, 4, 5 are sorted.
- [```1, 2, 3, 4, 5```] - 2 has been inserted into a sorted position and now the whole array is sorted.

- This is why it is called insertion sort, we are taking an element and inserting it into the correct spot.

## Insertion sort pseudocode
- start by picking the second element in the list.
- Compare it to the one before it and swap if necessary.
- Continue to the next element and if it is in the incorrect order, iterate through the sorted portion (i.e. the left side) to place the element in the correct position.
- Repeat until the list is sorted and return that list.

```python
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
```

## Insertion sort Big O
- It technically runs in O(n^2)