Recursion is a process (mostly a function) that calls itself.

- functions called other functions, but functions can also call themselves.
- There has to be some endpoint.

## Applications of recursion
- Used in JSON.parse/JSON.stringify.
- document.getElementById and DOM traversal algorithms
- Object traversal
- Used in complex data structures like trees and graphs.
- It is sometimes a cleaner alternative to iteration.

_Using recursion as an alternative to a loop to print list elements_
```python
def print_array_element(list, i):
    list_length = len(list)
    print(list[i])
    i += 1
    if i >= list_length:
        return
    print_array_element(list, i)

print_array_element([1, 2, 3, 4, 5], 0)
```

## The Call Stack
In almost all programming languages, there is a built in data structure that manages what happens when functions are invoked.

It is called **The call stack**

Any time a function is invoked, it is placed (pushed) on the top of the call stack.

When the compiler sees the return keyword or when the function ends, the compiler will remove (pop) the top item from the stack.

## How recursive functions work

- Invoke the same function with a different input until you reach your **base case**.
- **BASE CASE** - is the condition when the recursion ends. This is the most important thing to understand in recursion.

## Where things can go wrong in recursion
- Forgetting the base case.
- Returning the wrong thing or even returning the correct thing too early.
- Stack Overflow (```Max call stack exceeded``` is the error shown for most languages)