"""Challenge 11"""
from read_from_file import get_input_data


def format_data(lines: list[str]) -> list[list[int]]:
    """Turns the data into a grid of ints."""

    return [list(map(int, line.split(" "))) for line in lines]


if __name__ == "__main__":

    input_data = get_input_data(11)
    print(format_data(input_data))
