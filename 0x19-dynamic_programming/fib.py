"""Implementation of fibonacci without dynamic programming"""
def fib(n):
    """Finds the nth element in a fibonacci sequence"""
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)
print(fib(500))