"""Problem 11
    Given a grid of numbers, what is the largest product of 4 numbers on a line?
    The line can be horizontal, vertical, or diagonal."""
from read_from_file import get_input_data


def format_data(lines: list[str]) -> list[list[int]]:
    """Turns the data into a grid of ints."""

    return [list(map(int, line.split(" "))) for line in lines]


def find_max_product_in_line(line: list[int]) -> int:
    """Finds the highest product of 4 consecutive numbers in a list."""

    if len(line) < 4:
        print(line)

    products = [line[i]*line[i+1]*line[i+2]*line[i+3]
                for i in range(0, len(line)-3)]

    return max(products)


def find_max_horizontal(grid: list[list[int]]) -> int:
    """Finds the highest 4-product within the rows of a grid."""

    max_per_row = [find_max_product_in_line(row)
                   for row in grid]

    return max(max_per_row)


def find_max_vertical(grid: list[list[int]]) -> int:
    """Finds the highest 4-product within the rows of a grid."""

    grid_transposed = [[grid[j][i] for j in range(0, len(grid))]
                       for i in range(0, len(grid[0]))]

    return find_max_horizontal(grid_transposed)


def get_pos_line(grid: list[list[int]], start_row: int, start_col: int) -> list[int]:
    """Returns a line in the grid with gradient 1, starting from a given point."""

    col_max = len(grid[0])

    line = []

    row = start_row
    col = start_col

    while row >= 0 and col < col_max:
        line.append(grid[row][col])
        row -= 1
        col += 1

    return line


def get_all_pos_lines(grid: list[list[int]]) -> list[list[int]]:
    """Returns all diagonal lines of positive gradient, with length > 3."""

    start_coords = [(i, 0) for i in range(3, len(grid))]
    start_coords.extend([(19, j) for j in range(1, len(grid[0])-3)])

    return [get_pos_line(grid, coord[0], coord[1])
            for coord in start_coords]


def get_neg_line(grid: list[list[int]], start_row: int, start_col: int) -> list[int]:
    """Returns a line in the grid with gradient -1, starting from a given point."""

    col_max = len(grid[0])
    row_max = len(grid)

    line = []

    row = start_row
    col = start_col

    while row < row_max and col < col_max:
        line.append(grid[row][col])
        row += 1
        col += 1

    return line


def get_all_neg_lines(grid: list[list[int]]) -> list[list[int]]:
    """Returns all diagonal lines of positive gradient, with length > 3."""

    start_coords = [(0, i) for i in range(0, len(grid[0])-3)]
    start_coords.extend([(j, 0) for j in range(1, len(grid)-3)])

    return [get_neg_line(grid, coord[0], coord[1])
            for coord in start_coords]


if __name__ == "__main__":

    input_data = get_input_data(11)
    grid = format_data(input_data)

    max_hor = find_max_horizontal(grid)
    max_ver = find_max_vertical(grid)
    max_diag_pos = find_max_horizontal(get_all_pos_lines(grid))
    max_diag_neg = find_max_horizontal(get_all_neg_lines(grid))

    print(max([max_hor, max_ver, max_diag_neg, max_diag_pos]))
