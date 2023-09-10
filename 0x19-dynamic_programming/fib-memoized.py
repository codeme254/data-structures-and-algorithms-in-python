def fib(n, memo={}):
    # check if the memo dictionary has key n defined
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    result = fib(n-1, memo) + fib(n-2, memo)
    memo[n] = result
    print(memo)
    return result

print(fib(100))
