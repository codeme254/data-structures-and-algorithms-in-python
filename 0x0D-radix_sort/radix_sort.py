"""Implementation of the radix sort algorithm"""

from typing import List

# possible pitfalls
    # convert number back to number data type in get_digit
    # return a number data type in get_digit

def get_digit(number: int, place: int):
    """Returns digit from the number at a given place"""
    # get_digit(12345, 0) returns 5
    number_str = str(number)
    if place >= len(number_str):
        return 0
    reversed_str: str = ""
    i: int = len(number_str) - 1
    while i >= 0:
        reversed_str += number_str[i]
        i -= 1
    return reversed_str[place]
    
def digit_count(number: int):
    """Returns the length of an integer number"""
    return len(str(number))

def most_digits(numbers: List[int]):
    """Returns the number of digits in the largest numbers in the list"""
    most_numbers_length = 0
    for number in numbers:
        current_count = digit_count(number)
        if current_count > most_numbers_length:
            most_numbers_length = current_count
    return most_numbers_length

def radix_sort(lst: List[int]):
    """Sorts a list of positive integer values using the radix sort algorithm"""
    largest_range = most_digits(lst)
    for i in range(0, largest_range):
        buckets = [[] for i in range(0, 10)]
        for number in lst:
            current_digit = int(get_digit(number, i)) ## 3221 - 1
            buckets[current_digit].append(number)
        lst = [element for sublist in buckets for element in sublist]
    return lst
