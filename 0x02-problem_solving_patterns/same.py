# Write a function called same which accepts two lists. The function should return true if every value in the array has it's corresponding value squared in the second array. The frequency of values must be the same.
# - same([1, 2, 3], [4, 1, 9]) True
# - same([1, 2, 3], [1, 9]) False
# - same([1, 2, 1], [4, 4, 1]) False

def same(list1, list2):
    if len(list1) > len(list2):
        return False
    lookup = {}
    for element in list1:
        square = element * element
        try:
            correct_index = list2.index(square)
        except(ValueError):
            return False
        finally:
            list2.remove(square)
    return True

print(same([1, 2, 3], [4, 1, 9]))
print(same([1, 2, 3], [1, 9]))
print(same([1, 2, 1], [4, 4, 1]))