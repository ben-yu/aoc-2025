def part_one(filename):
    fit = 0
    with open(filename) as f:
        for line in f:
            if "x" in line:
                dimensions, boxes = line.split(":")
                w,h = dimensions.split("x")
                area = int(w)//3 * int(h)//3

                totalboxes = sum(int(x) for x in boxes.split())
                if totalboxes <= area:
                    fit += 1
        print(fit)

part_one("data/examples/12.txt")
part_one("data/inputs/12.txt")
