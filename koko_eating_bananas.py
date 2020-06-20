# https://leetcode.com/problems/koko-eating-bananas/

import math


def can_finish(piles, speed, total_hrs):
    hour_completed = 0
    for bananas_in_pile in piles:
        total_rounds = math.ceil(bananas_in_pile / speed)
        hour_completed += total_rounds
        # print(total_rounds)
    return hour_completed <= total_hrs


def min_eating_speed(piles, hour, low, high):
    mid = low + (high - low) // 2

    if low > high:
        return mid

    if mid == 1:
        return mid

    if can_finish(piles, mid, hour):
        # if mid == 1:
        #     return mid
        if can_finish(piles, mid - 1, hour):
            return min_eating_speed(piles, hour, low, mid - 1)
        else:
            return mid
    else:
        return min_eating_speed(piles, hour, mid + 1, high)


input_data = [
    {"piles": [3, 6, 7, 11], "H": 8, "output": 4},
    {"piles": [30, 11, 23, 4, 20], "H": 5, "output": 30},
    {"piles": [30, 11, 23, 4, 20], "H": 6, "output": 23}
]

for data in input_data:
    result = min_eating_speed(data['piles'], data['H'], 1, max(data['piles']))
    assert result == data['output']

#
# speed = 1
#
# for speed in range(1, max(piles) + 1):
#     print("speed :", speed)
#     print(can_complete_all_piles(piles, speed, hour))
#


# [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]

# pl1 -> 1 [3]
# pl1 -> 2 [2]
# pl1 -> 3 [1]

# pl2 -> 4 [6]
# pl2 -> 5 [5]
# pl2 -> 6 [4]
# pl2 -> 7 [3]
# pl2 -> 8 [2]
# pl2 -> 9 [1]

# pl3 -> 9 [7]
# pl3 -> 10 [6]
# pl3 -> 16 [1]

# pl4 -> 17 [11]
# pl4 -> 27 [1]

# 27, 15, 10, 8 , 8, 6, 4
