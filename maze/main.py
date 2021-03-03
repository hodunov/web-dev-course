from sys import setrecursionlimit

maze = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
        ['#', '#', '#', '#', '#', '#', '.', '#', '#', '#'],
        ['#', '.', '.', '.', '.', '.', '.', '#', '#', '#'],
        ['#', '.', '#', '#', '#', '#', '.', '#', '#', '#'],
        ['#', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
        ['#', '#', '.', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '#', '.', '#', '#', '.', '#', '#', '#', '#'],
        ['#', '#', '.', '#', '#', '#', '#', '.', '#', '#']]


def is_exit_here(x, y):
    """
    Function will check if the coordinates match the coordinates of the exit
    :param x: list coordinate
    :param y: item coordinate in the list
    :return: locations dict
    """
    # possible exit positions for x or y
    if x == N - 1 or y == 0 or x == 0 or y == NN - 1:
        # Skip entry coordinates
        if locations["enter"] != [x, y]:
            # There may be more than one exit, so let's add all of them
            locations["exit"].append([x, y])
    return locations


def solve(maze, x, y, visited):
    """
    Finding an exit of the maze
    :param maze: NxN matrix
    :param x (int): list coordinate
    :param y (int): item coordinate in the list
    :param visited: size duplicate maze
    """
    if maze[x][y] == '.':
        # mark the current cell as visible
        visited[x][y] = True

        # check exit
        is_exit_here(x, y)
        # down
        if x + 1 < N and not visited[x + 1][y]:
            solve(maze, x + 1, y, visited)
        # up
        if x - 1 >= 0 and not visited[x - 1][y]:
            solve(maze, x - 1, y, visited)
        # right
        if y + 1 < NN and not visited[x][y + 1]:
            solve(maze, x, y + 1, visited)
        # left
        if y - 1 >= 0 and not visited[x][y - 1]:
            solve(maze, x, y - 1, visited)

    return visited


if __name__ == '__main__':
    # Set the maze entrance coordinates
    enter = [1, 0]
    # Main list length
    N = len(maze)
    # Internal list length
    NN = len(maze[0])
    # Different variants of maze are being considered.
    # It is necessary to prevent RecursionError.
    # I don't think making recursion infinite is a good idea, so I'll try increasing it as follows:
    setrecursionlimit(1000 + N * N)

    # matrix - a duplicate of the maze to follow the path.
    visited = [[False for x in range(NN)] for y in range(N)]

    # Save the entrance and exit to the maze in dict
    locations = {"enter": enter, "exit": []}

    # Find a solution
    solve(maze, enter[0], enter[1], visited)

    if not locations['exit']:
        print("Buddy, it's really bad. This maze has no way out. I hope you're ready for the walk back 😞")
    else:
        print("Yay! It was a challenge, but we did it!'🎉\nExit location:", *locations['exit'], sep='\n')
