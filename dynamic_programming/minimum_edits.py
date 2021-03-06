def minimun_edits_stack(X, Y, m, n):
    if m == 0:
        return n
    if n == 0:
        return m
    if X[m - 1] == Y[n - 1]:
        return minimun_edits_stack(X, Y, m - 1, n - 1)
    return 1 + min(minimun_edits_stack(X, Y, m - 1, n),
                   minimun_edits_stack(X, Y, m, n - 1),
                   minimun_edits_stack(X, Y, m - 1, n - 1))


X = 'Sunday'
Y = 'Saturday'
result = minimun_edits_stack(X, Y, len(X), len(Y))
print(result)
X = 'Cat'
Y = 'Cap'
result = minimun_edits_stack(X, Y, len(X), len(Y))
print(result)

# Convert X to Y
def minimun_edits(X, Y):
    m = len(X) + 1
    n = len(Y) + 1
    dp_arr = [[0] * n for i in range(m)]
    for i in range(m):
        for j in range(n):
            # if X is empty then we have to copy all items from Y
            if i == 0:
                dp_arr[i][j] = j  # insert
            # if Y is empty then we have to delete all items from X
            elif j == 0:
                dp_arr[i][j] = i  # delete
            # If X and Y are same, then no insert/delete/replace operation is required.
            elif X[i - 1] == Y[j - 1]:
                dp_arr[i][j] = dp_arr[i - 1][j - 1]
            # take m
            else:
                dp_arr[i][j] = 1 + min(dp_arr[i - 1][j],  # insert
                                       dp_arr[i][j - 1],  # delete
                                       dp_arr[i - 1][j - 1])  # replace

    # print(dp_arr)
    return dp_arr[m - 1][n - 1]


X = 'Sunday'
Y = 'Saturday'
result = minimun_edits(X, Y)
print(result)

X = 'Cat'
Y = 'Cap'
result = minimun_edits(X, Y)
print(result)
