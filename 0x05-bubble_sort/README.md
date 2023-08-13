# Bubble sort
- A sorting algorithm that takes larger values to the end of the list in each pass (can also be smaller values being taken to the end depending on how we write the code).
- ```Largest values bubble up to the top```

## Bubble sort pseudocode
- Create a function that takes in a list to be sorted and returns that list.
- Start looping with a variable called i at the end of the list towards the beginning.
- start an inner loop with a variable called j from the beginning until i-1.
- If list[j] is greater than list[j+1], swap those two values.
- Return the sorted array.

```py
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
```

## Big O of bubble sort
it is n squared in general, if the data is nearly sorted, it would look like linear time but still we will be making a number of passes and doing several comparisons.