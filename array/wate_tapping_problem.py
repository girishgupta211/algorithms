def find_water(arr, n):
    # left[i] contains height of tallest bar to the left of i'th bar including itself
    left = [0] * n

    # Right [i] contains height of tallest bar to the right of ith bar including itself
    right = [0] * n

    # Initialize result 
    water = 0

    # Fill left array. start from beginning
    left[0] = arr[0]
    for i in range(1, n):
        left[i] = max(left[i - 1], arr[i])

    # Fill right array. start from end
    right[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        right[i] = max(right[i + 1], arr[i])

    # Calculate the accumulated water element by element consider the amount of water on i'th bar, the
    # amount of water accumulated on this particular bar will be equal to min(left[i], right[i]) - arr[i] .
    for i in range(0, n):
        water += min(left[i], right[i]) - arr[i]

    return water


# Driver program 

arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
n = len(arr)
print("Maximum water that can be accumulated is", find_water(arr, n))
