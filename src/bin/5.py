from intervaltree import Interval, IntervalTree

fresh_intervals = IntervalTree()
intervals_done = False
fresh_count = 0

with open('data/examples/05.txt') as f:
    lines = f.readlines()
    for line in lines:
        if line == "\n":
            intervals_done = True
            continue
        # parse intervals until empty line
        if not intervals_done:
            x, y = line.split('-')
            fresh_intervals[int(x):int(y)+1] = line
        else:
            res = int(line.strip())
            if fresh_intervals[res]:
                #print(res)
                fresh_count += 1

    fresh_intervals.merge_overlaps()
    interval_count = 0
    for interval in fresh_intervals:
        interval_count += interval.end - interval.begin


    print("Solution 1: {}".format(fresh_count))
    print("Solution 2: {}".format(interval_count))


