from inputs.data_load import input_data_map


input_lines = input_data_map(1, lambda row: int(row if row else None))


if __name__ == "__main__":
    totals = [0]
    for line in input_lines:
        if line is None:
            totals.append(0)
        else:
            totals[-1] += line
    print(f"Highest calories: {max(totals)}")
    print(f"Total of three most calorific elves: {sum(sorted(totals, reverse=True)[:3])}")
