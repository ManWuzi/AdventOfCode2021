import sys
import numpy as np
from collections import Counter, defaultdict

if len(sys.argv) != 2:
    print("python %s <input_file>" %sys.argv[0])
    sys.exit(0)

with open(sys.argv[1], "r") as day5_file:
    lines = day5_file.readlines()

    all_points = []
    diagonals = []
    for line in lines:
        ends = line.split("->")
        if ends[0].strip().split(",")[0] == ends[1].strip().split(",")[0]:
            start, end = int(ends[0].strip().split(",")[1]), int(ends[1].strip().split(",")[1])
            direction = 1 if start < end  else -1
            d_range = range(start, end+1, 1) if direction == 1 else range(start, end-1, -1)
            for i in d_range:
                all_points.append((int(ends[0].strip().split(",")[0]), i))

        if ends[0].strip().split(",")[1] == ends[1].strip().split(",")[1]:
            start, end = int(ends[0].strip().split(",")[0]), int(ends[1].strip().split(",")[0])
            direction = 1 if start < end  else -1
            d_range = range(start, end+1, 1) if direction == 1 else range(start, end-1, -1)
            for i in d_range:
                all_points.append((i, int(ends[0].strip().split(",")[1])))

        if ends[0].strip().split(",")[1] != ends[1].strip().split(",")[1] and ends[0].strip().split(",")[0] != ends[1].strip().split(",")[0]:
            start_1, end_1, start_2, end_2 = int(ends[0].strip().split(",")[0]), int(ends[0].strip().split(",")[1]), int(ends[1].strip().split(",")[0]), int(ends[1].strip().split(",")[1])
            direction_1, direction_2 = 1 if start_1 < start_2  else -1, 1 if end_1 < end_2  else -1
            d_range1 = range(start_1, start_2+1, 1) if direction_1 == 1 else range(start_1, start_2-1, -1)
            d_range2 = range(end_1, end_2+1, 1) if direction_2 == 1 else range(end_1, end_2-1, -1)

            for x,y in zip(d_range1, d_range2):
                diagonals.append((x,y))

    all_points_c = Counter(all_points)
    print("Part 1 solution: %d" %len(list(filter(lambda x: x >= 2, all_points_c.values()))))

    diagonals_c = Counter(all_points + diagonals)
    print("Part 2 solutions: %d" %len(list(filter(lambda x: x >= 2, diagonals_c.values()))))