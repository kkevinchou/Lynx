def print_grid(grid):
    width = len(grid)
    height = len(grid[0])

    for y in range(height):
        print [grid[x][y] for x in range(width)]
