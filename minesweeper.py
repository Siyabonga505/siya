# Create a function that takes a grid of '#', '-'
def count_adjecent_mines(grid):
    # Dimensions of the grid
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    # Initialize the output grid
    output_grid = [['0' for _ in range(cols)] for _ in range(rows)]

    # Directions for adjecent positions
    directions = [
        (-1, -1), (-1, 0), (-1, 1), # NW, N, NE
        (0, -1),           (0, 1),  #W,      E
        (1, -1), (1, 0),    (1, 1)  #SW,   S,   SE
    ]

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == '#':
                # Mark mine in the output grid
                output_grid[row][col] = '#'

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    # Check for valid indices
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '-':
                        output_grid[nr][nc] = str(int(output_grid[nr][nc]) + 1)
    return output_grid

# Example usage
input_grid = [
      ["-", "-", "-", "#", "#"],
      ["-", "#", "-", "-", "-"],
      ["-", "-", "#", "-", "-"],
      ["-", "#", "#", "-", "-"],
      ["-", "-", "-", "-", "-"]
]

output_grid = count_adjecent_mines(input_grid)
for row in output_grid:
    print(row)
