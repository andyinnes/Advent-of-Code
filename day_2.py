from io import open
from pathlib import Path


input_file = Path(__file__).parent / "inputs" / "day_2.txt"
with open(input_file, "r") as file:
    input_lines_str = file.read().split("\n")


shape_score = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}
scoring = [6, 3, 0]
score_map = {
    "X": ["C", "A", "B"],
    "Y": ["A", "B", "C"],
    "Z": ["B", "C", "A"],
}


def score_round(elf: str, me: str) -> int:
    shape = shape_score[me]
    game = scoring[score_map[me].index(elf)]
    return shape + game


def identify_shape(elf: str, outcome: str) -> str:
    pos = ["Z", "Y", "X"].index(outcome)
    k = ""
    for k, v in score_map.items():
        if v.index(elf) == pos:
            break
    return k


if __name__ == "__main__":
    input_lines = [line.split() for line in input_lines_str]
    total_score = 0
    for elf, me in input_lines:
        total_score += score_round(elf, me)
    print(f"Total score part 1: {total_score}")

    total_score_2 = 0
    for elf, outcome in input_lines:
        me = identify_shape(elf, outcome)
        total_score_2 += score_round(elf, me)
    print(f"Total score part 2: {total_score_2}")
