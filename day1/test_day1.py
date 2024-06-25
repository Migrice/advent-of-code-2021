from day1 import day1_part1, day1_part2

def test_day1_part1_give_1():
    assert(day1_part1([199,200])) == 1

def test_day1_part1_give_2():
    assert(day1_part1([199,200,208])) == 2

def test_day1_part1_give_3():
    assert(day1_part1([199, 200, 208, 210])) == 3

def test_day1_part1_give_3_when_decreased():
    assert(day1_part1([199, 200, 208, 210, 200])) == 3

def test_day1_part1_give_7():
    assert(day1_part1([199, 200, 208, 210, 200, 207, 240, 269, 260, 263])) == 7


def test_day1_part2():
    assert(day1_part2([199,200,208,210,200,207,240,269,260,263])) == 5