
def day1_part1(data: list[int]) -> int:
    result = 0
    for i in range((len(data)) -1):
        if data[i+1] > data[i]:
            result +=1

    return result

def day1_part2(data:list[int]) -> int:

    sum_list = []
    for i in range(len(data) -2):
        sum_list.append(data[i]+data[i+1]+data[i+2])

    result = day1_part1(sum_list)

    return result


