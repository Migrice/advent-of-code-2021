from .day1 import day1_part1, day1_part2


def run_day1():
    with open("day1/data_part_1.txt", "r") as file:
        data = file.readlines()

    data = [int(character.strip()) for character in data]
    result = day1_part1(data)
    print("Day 1 Part 1 >>>>>>>>>>>>>>>>>>>>>>", result)


    with open("day1/data_part_2.txt", "r") as f:
        part_data = f.readlines()

    part2_data = [int(character.strip()) for character in part_data]
    result2 = day1_part2(part2_data)

    print("Day 1 part 2 >>>>>>>>>>>>>>>>>>>>>>", result2)
