# https://www.geeksforgeeks.org/number-buildings-facing-sun/


# if sun is in left side
def building_facing_sun(arr):
    highest_height = arr[0]
    total_buildings = 1
    for i in range(1, len(arr)):
        if arr[i] > highest_height:
            total_buildings += 1
            highest_height = arr[i]

    return total_buildings


print(building_facing_sun([7, 4, 8, 2, 9]))


# sun is in the right direction
def building_facing_sun_using_stack(arr):
    stack = [arr[0]]
    for i in range(1, len(arr)):
        next_building = arr[i]

        # pop all previous_buildings from stack
        while stack and next_building > stack[-1]:
            stack.pop()

        stack.append(next_building)
    return stack


arrs = [[7, 4, 8, 2, 9], [9, 7, 4, 8, 2], [4, 3, 2, 1], [1, 2, 3, 4]]
for arr in arrs:
    print(building_facing_sun_using_stack(arr))
