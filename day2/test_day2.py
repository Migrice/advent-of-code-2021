from day2 import day2_part1

def test_day2_part1_forward_5():
    assert(day2_part1(["forward 5"])) == 0

def test_day2_part1_forward_5_down_5():
    assert(day2_part1(["forward 5","down 5"])) == 25

def test_day2_part1_forward_5_down_5_forward_8():
    assert(day2_part1(["forward 5","down 5","forward 8"])) == 65