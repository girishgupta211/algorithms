import timeit


def fibonacci_dp(n):
    arr = []
    for i in range(n + 1):
        arr.append(0)

    print(arr)
    arr[1] = 1

    if n in (0, 1):
        return arr[n]

    for i in range(2, n + 1):
        arr[i] = arr[i - 1] + arr[i - 2]

    print(arr)
    return arr[n]


starttime = timeit.default_timer()
res = fibonacci_dp(40)
print("The time difference is using DP:", timeit.default_timer() - starttime)

print(res)

# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155]
# The time difference is using DP: 6.948499999999934e-05

def fibonacci(n):
    if n < 0:
        return "invalid input"

    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


starttime = timeit.default_timer()
res = fibonacci(40)
print("The time difference is using recursion :", timeit.default_timer() - starttime)
print(res)

# The time difference is using recursion : 59.729086562999996

