
"""This code creates a mine grid represented by a 2D list, where the "#" symbol represents a mine and the "-" symbol
represents an empty cell.The code then calculates the number of mines surrounding each empty cell and replaces
the "-" symbol with the number of surrounding mines. The modified grid is then printed to the console."""


def count_adjacent_mines(mine_grid):

    # Created a 2D list to store the counts of adjacent mines for each cell
    adjacent_mine_counts = []
    for i in range(len(mine_grid)):
        row = []
        for j in range(len(mine_grid[i])):
            row.append(0)
        adjacent_mine_counts.append(row)

    # Loop through each cell in the mine grid
    for i, row in enumerate(mine_grid):
        for j, cell in enumerate(row):

            # If the current cell contains a mine
            if cell == "#":

                # Loop through each adjacent cell
                for x in range(i-1, i+2):
                    for y in range(j-1, j+2):

                        # If the adjacent cell is within the bounds of the mine grid and doesn't contain a mine
                        if 0 <= x < len(mine_grid) and 0 <= y < len(mine_grid[x]) and mine_grid[x][y] != "#":
                            # Increment the count of adjacent mines for the adjacent cell
                            adjacent_mine_counts[x][y] += 1

    # Loop through each cell in the mine grid again
    for i, row in enumerate(mine_grid):
        for j, cell in enumerate(row):

            # If the current cell doesn't contain a mine
            if cell == "-":
                # Setting the value of the cell to the count of adjacent mines
                mine_grid[i][j] = str(adjacent_mine_counts[i][j])

    return mine_grid


mine_grids = [["-", "-", "-", "#", "#"],
              ["-", "#", "-", "-", "-"],
              ["-", "-", "#", "-", "-"],
              ["-", "#", "#", "-", "-"],
              ["-", "-", "-", "-", "-"]]

result = count_adjacent_mines(mine_grids)
for rows in result:
    print(rows)
