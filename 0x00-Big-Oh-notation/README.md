# The Big O Notation

- Imagine we have multiple implementations of the same function.

- How do we determine which function is the best.

This is what Big O notation is, it is a system, a way of generalizing code and talking about it and comparing its performance with another code.

## who cares
- it is important to have a precise vocabulary to talk about how our code performs.
- Useful for discussing trade offs between various approaches.
- When your code slows down or crashes, identifying parts of the code that are inefficient can help us find pain points in our applications.

## The problem with time (why not use time to measure efficiency of algorithms)
- Different machines will record different times.
- The same machine will record different times.
- For fast algorithms, speed measurements may not be fast enough.

## Counting operations
- Better than counting time

Consider the examples below, they are both functions adding from 0 up to and including n
```python
def add_upto(n):
    total = 0
    for i in range(0, n+1):
        total += i
    return total
# n additions
# n assignments
# 1 assignment
# 1 assignment
# n comparisons
# n additions and assignments
```

```python
def add_upto(n):
    return n * (n + 1) / 2
# 3 operations (*, + and /)
```

- Counting is also hard.


## The Big o notation
- is a way to formalize fuzzy counting.
- It allows us to talk about the runtime of algorithms as inputs grow.
- Usually, we don't care about the other details, only the trends.

We say that an algorithm is ```O(f(n))``` if the number of simple operations the computer has to do is eventually less than a constant times ```f(n)```, as n increases.

- f(n) could be linear ```f(n) = n```
- could be quadratic ```f(n) = n^2```
- f(n) could be constant ```f(n) = 1```
- could be something entirely different.

When we talk about Big O, we are talking about the worst case scenario of our code.

## Simplifying Big O expressions
1. Constant don't matter - O(2n) is O(n), O(500) is O(1), O(13n^2) is O(n^2)
1. Smaller terms don't matter, i.e O(n + 10) is O(n), O(n^2 + 5n + 8) is O(n^2).
1. Arithmetic operations are constant i.e 2 + 2 is same as 10000000 + 10000000 in terms of computer speed
1. Variable assignment is constant.
1. Accessing elements in an array (by index) or object (by key) is constant.
1. In a loop, the complexity is the length of the loop multiplied by whatever is happening in the loop.

O(1) > O(log n) > O(n) > O(n log n) > O(n^2).

## Space Complexity
- We can also use Big O notation to analyze space complexity of an algorithm (the amount of memory).

- - Most primitives (booleans, numbers etc) are constant space.
- - Strings require O(n) space where n is the length of the string.
- - Reference types are generally O(n), where n is the length (for lists) and the number of keys (for dictionaries)