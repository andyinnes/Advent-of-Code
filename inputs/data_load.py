from io import open
from pathlib import Path


def input_data(day):
    input_file = Path(__file__).parent / f"day_{day}.txt"
    with open(input_file, "r") as file:
        input_lines_str = file.read().split("\n")
    return input_lines_str


def input_data_split(day, split = None):
    data = input_data(day)
    if split is None:
        return [line.split() for line in data]
    else:
        return [line.split(split) for line in data]


def input_data_map(day, callable):
    data = input_data(day)
    return [callable(row) for row in data]
