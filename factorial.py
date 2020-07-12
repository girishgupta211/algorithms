import timeit


def factorial_dp(n):
    arr = []
    for i in range(n + 1):
        arr.append(0)

    print(arr)
    arr[0] = 1

    for i in range(1, n + 1):
        arr[i] = i * arr[i - 1]

    print(arr)
    return arr[n]


starttime = timeit.default_timer()
res = factorial_dp(100)
print(res)
print("The time difference is using DP:", timeit.default_timer() - starttime)


def factorial(n):
    if n < 0:
        return "invalid input"

    if n == 0:
        return 1

    return n * factorial(n - 1)


starttime = timeit.default_timer()
res = factorial(100)
print(res)
print("The time difference is using recursion:", timeit.default_timer() - starttime)
