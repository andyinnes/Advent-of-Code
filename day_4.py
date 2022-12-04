from io import open
from pathlib import Path


input_file = Path(__file__).parent / "inputs" / "day_4.txt"
with open(input_file, "r") as file:
    input_lines_str = file.read().split("\n")

input_pairs = [inp.split(",") for inp in input_lines_str]
input_bounds = [
    tuple(tuple(map(int, elf.split("-"))) for elf in elf_row) for elf_row in input_pairs
]


if __name__ == "__main__":
    count = 0
    for left_elf, right_elf in input_bounds:
        if left_elf[0] >= right_elf[0] and left_elf[1] <= right_elf[1]:
            count += 1
        elif right_elf[0] >= left_elf[0] and right_elf[1] <= left_elf[1]:
            count += 1
    print(f"Fully contained pairs: {count}")

    count = 0
    for left_elf, right_elf in input_bounds:
        if right_elf[0] <= left_elf[1] <= right_elf[1] or left_elf[0] <= right_elf[1] <= left_elf[1]:
            count += 1
    print(f"Overlapping pairs: {count}")
