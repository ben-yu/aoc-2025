def parse_input(filename):
    """Parse input file to get list of red tile coordinates."""
    with open(filename) as f:
        tiles = []
        for line in f:
            line = line.strip()
            if line:
                x, y = map(int, line.split(','))
                tiles.append((x, y))
        return tiles


def part_one(filename):
    """Find the largest rectangle using any two red tiles as opposite corners."""
    tiles = parse_input(filename)
    max_area = 0

    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            x1, y1 = tiles[i]
            x2, y2 = tiles[j]
            # Area includes both corner tiles
            area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
            max_area = max(max_area, area)

    return max_area



if __name__ == "__main__":
    print("Example Part One:", part_one('data/examples/09.txt'))
    print("Part One:", part_one('data/inputs/09.txt'))
