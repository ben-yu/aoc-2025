from collections import defaultdict
from functools import reduce


def part_one():
    with open('data/inputs/06.txt') as f:
        lines = f.readlines()

        tracker = defaultdict(list)
        answer = 0
        for l in range(len(lines)):
            line = lines[l]
            nums = line.strip().split()
            # operands
            if l == len(lines) - 1:
                for i, n in enumerate(nums):
                    if n == "+":
                        answer += reduce(lambda x, y: x + y, tracker[i])
                    elif n == "*":
                        answer += reduce(lambda x, y: x * y, tracker[i])
            else:
                for i, n in enumerate(nums):
                    tracker[i].append(int(n))
        print("Solution 1: {}".format(answer))

def part_two():
    with open('data/inputs/06.txt') as f:
        grid = []
        lines = f.readlines()
        for l in lines:
            grid.append(list(l.rstrip('\n')))

        tracker = defaultdict(list)
        cur_index = 1
        answer = 0
        for x in reversed(range(len(grid[0]))):
            res = []
            for y in range(len(grid)):
                if grid[y][x] == '+':
                    tracker[cur_index].append(int("".join(res)))
                    res = []
                    answer += reduce(lambda a, b: a + b, tracker[cur_index])
                    #print(tracker[cur_index])
                    cur_index += 1
                elif grid[y][x] == '*':
                    tracker[cur_index].append(int("".join(res)))
                    res = []
                    answer += reduce(lambda a, b: a * b, tracker[cur_index])
                    #print(tracker[cur_index])
                    cur_index += 1
                elif grid[y][x] != ' ':
                    res.append(grid[y][x])
            if len(res) > 0:
                tracker[cur_index].append(int("".join(res)))

        print("Solution 2: {}".format(answer))

part_one()
part_two()

