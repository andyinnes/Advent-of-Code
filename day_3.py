from inputs.data_load import input_data

input_lines_str = input_data(3)

def letter_priority(letter: str) -> int:
    order = ord(letter)
    if order >= 97:
        return order - 96
    else:
        return order - 38

def find_matching_item(item_list):
    mid = int(len(item_list) / 2)
    item = list(set(item_list[:mid]).intersection(item_list[mid:]))[0]
    return item


def find_group_badge(rucksack_list):
    base = set(rucksack_list[0])
    for rucksack in rucksack_list[1:]:
        base.intersection_update(rucksack)
    return list(base)[0]


if __name__ == "__main__":
    total_prio = 0
    for sack in input_lines_str:
        match = find_matching_item(sack)
        score = letter_priority(match)
        total_prio += score
    print(f"Total priority part 1: {total_prio}")

    total = 0
    group_size = 3
    for i in range(int(len(input_lines_str) / group_size)):
        pos = i * group_size
        match = find_group_badge(input_lines_str[pos : pos + group_size])
        score = letter_priority(match)
        total += score
    print(f"Total priority part 2: {total}")
