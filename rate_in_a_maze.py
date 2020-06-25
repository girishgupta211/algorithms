maze = [[1, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 1, 0, 0],
        [1, 1, 1, 1]]

print(maze)

# Recursion --> Base condition
# if there is any mistake --> backtrack
# Can move in any direction
# keep visited matrix

M = 4
N = 4
visited = [[0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0]]


def can_visit(x, y):
    # check if coordinates are within matrix
    if x < 0 or x == M or y < 0 or y == N:
        return False

    # check for NOT visited and 0 entry
    if visited[x][y] == 1 or maze[x][y] == 0:
        return False

    return True


def solve_rate_in_maze(x, y):
    if x == M - 1 and y == N - 1:
        return True

    # Upside
    if can_visit(x - 1, y):
        visited[x - 1][y] = 1
        result = solve_rate_in_maze(x - 1, y)
        if result is False:
            visited[x - 1][y] = 0

    # left
    can_visit(x, y - 1)

    # down
    can_visit(x + 1, y)

    # right
    can_visit(x, y + 1)


solve_rate_in_maze(0, 0)
# result = can_visit(1, 1)
# print(result)
