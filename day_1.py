from io import open
from pathlib import Path


input_file = Path(__file__).parent / "inputs" / "day_1.txt"
with open(input_file, "r") as file:
    input_lines_str = file.read().split("\n")
input_lines = [int(line) if line else None for line in input_lines_str]


if __name__ == "__main__":
    totals = [0]
    for line in input_lines:
        if line is None:
            totals.append(0)
        else:
            totals[-1] += line
    print(f"Highest calories: {max(totals)}")
    print(f"Total of three most calorific elves: {sum(sorted(totals, reverse=True)[:3])}")
