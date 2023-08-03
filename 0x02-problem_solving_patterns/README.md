Some problem solving patterns include:
- Frequency counter
- Multiple pointers
- Sliding window
- Divide and conquer
- Dynamic programming
- Greedy algorithms
- Backtracking
- MANY MORE!!!!

### Frequency counters
This pattern uses dictionaries or sets to collect values/frequencies of values.

This can often avoid the need for nested loops or O(N^2) operations with arrays and strings.

Write a function called same which accepts two lists.
The function should return true if every value in the array has it's corresponding value squared in the second array.
The frequency of values must be the same.
- same([1, 2, 3], [4, 1, 9]) True
- same([1, 2, 3], [1, 9]) False
- same([1, 2, 1], [4, 4, 1]) False

Given two strings, write a function to determine if the second string is an anagram of the first.
An anagram is a word, phrase or name formed by rearranging the letters of another eg cinema is formed from iceman


### Multiple pointers
Creating pointers or values that correspond to an index or position and move towards the beginning, end or middle based on a certain condition.

VERY efficient for solving problems with minimal space complexity as well.

### Sliding window
This pattern involves creating a window which can either be an array of number from one position to another.

Depending on a certain condition, the window either increases or close (and a new window is created)

Very useful for keeping track of a subset of data in an array/string etc.
