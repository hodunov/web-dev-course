maze = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
        ['#', '#', '#', '#', '#', '#', '.', '#', '#', '#'],
        ['#', '.', '.', '.', '.', '.', '.', '#', '#', '#'],
        ['#', '.', '#', '#', '#', '#', '.', '#', '#', '#'],
        ['#', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
        ['#', '#', '.', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '#', '.', '#', '#', '.', '#', '#', '#', '#'],
        ['#', '#', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['#', '#', '#', '#', '#', '#', '#', '.', '#', '#']]


def is_exit_here(x, y):
    """
    Function will check if the coordinates match the coordinates of the exit
    :param x: list coordinate
    :param y: item coordinate in the list
    :return: locations dict
    """
    # set two possible exit positions for x or y
    exit_coordinates = (0, N - 1)
    for i in exit_coordinates:
        # If at least one assumption fits, we have an exit
        if x == i or y == i:
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
        if y + 1 < N and not visited[x][y + 1]:
            solve(maze, x, y + 1, visited)
        # left
        if y - 1 >= 0 and not visited[x][y - 1]:
            solve(maze, x, y - 1, visited)

    return visited


if __name__ == '__main__':
    enter = [1, 0]

    N = len(maze)

    # matrix - a duplicate of the maze to follow the path.
    visited = [[False for x in range(N)] for y in range(N)]

    # Save the entrance and exit to the maze in dict
    locations = {"enter": enter, "exit": []}

    # Find a solution
    solve(maze, enter[0], enter[1], visited)

    if not locations['exit']:
        print("Buddy, it's really bad. This maze has no way out. I hope you're ready for the walk back 😞")
    else:
        print("Yay! It was a challenge, but we did it!'🎉\nExit location:", *locations['exit'], sep='\n')
