"""Challenge 11"""
from read_from_file import get_input_data


def format_data(lines: list[str]) -> list[list[int]]:
    """Turns the data into a grid of ints."""

    return [list(map(int, line.split(" "))) for line in lines]


def find_largest_product_in_line(line: list[int]) -> int:
    """Finds the largest product of 4 consecutive numbers in a single line."""

    max_index = 0
    for i in range(0, len(line) - 4):
        if line[i] < line[i+4]:
            max_index = i+1
    return line[max_index] * line[max_index+1] * line[max_index+2] * line[max_index+3]


if __name__ == "__main__":

    input_data = get_input_data(11)
    print(format_data(input_data))
