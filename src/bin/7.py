from collections import defaultdict

def part_one():
    with open('data/inputs/07.txt') as f:
        lines = f.readlines()

        grid = []

        for line in lines:
            grid.append(list(line.strip()))


        split_count = 0
        for x, line in enumerate(grid):
            for y, e in enumerate(line):
                # Split laser
                if e == '^' and x-1 >= 0 and (grid[x-1][y] == '|' or grid[x-1][y] == 'S'):
                    grid[x][y-1] = '|'
                    grid[x][y+1] = '|'
                    split_count += 1
                elif e == '.' and x-1 >= 0 and (grid[x-1][y] == '|' or grid[x-1][y] == 'S'):
                    grid[x][y] = '|'
        for x in grid:
            for e in x:
                print(e, end="")
            print('\n')
    print("Part One: {}".format(split_count))

def part_two():
    with open('data/inputs/07.txt') as f:
        lines = f.readlines()

        grid = []
        path_counts = defaultdict(int)

        for line in lines:
            grid.append(list(line.strip()))


        split_count = 0
        for x, line in enumerate(grid):
            for y, e in enumerate(line):
                # Split laser
                if e == '^' and x-1 >= 0 and (grid[x-1][y] == '|'):
                    grid[x][y-1] = '|'
                    path_counts[x,y-1] += path_counts[x-1, y]
                    grid[x][y+1] = '|'
                    path_counts[x,y+1] += path_counts[x-1, y]
                    split_count += 1
                if (e == '.' or e == '|') and x-1 >= 0 and (grid[x-1][y] == '|'):
                    grid[x][y] = '|'
                    path_counts[x,y] += path_counts[x-1,y]
                if e == '.' and x-1 >= 0 and (grid[x-1][y] == 'S'):
                    grid[x][y] = '|'
                    path_counts[x,y] = 1

        for i, x in enumerate(grid):
            for j, e in enumerate(x):
                print(e, end="")
            print('\n')
    answer = sum([path_counts[len(grid) - 1, x] for x in range(len(grid[0]))])
    print("Part Two: {}".format(answer))

part_one()
part_two()



