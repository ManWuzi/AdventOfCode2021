import sys

if len(sys.argv) != 2:
    print("python %s [day1_input]" %sys.argv[0])
    sys.exit(0)


with open(sys.argv[1], 'r') as day1_file:
    depths = list(map(int, day1_file.readlines()))
    increased, current = -1, 0
    for i in depths:
        if i > current:
            increased += 1
        current = i
    print("Part 1 solution: %d" %increased)

    increased, current = -1, 0
    for i in range(0, len(depths)-2):
        all_sum = sum(depths[i:i+3])
        if all_sum > current:
            increased+=1
        current = all_sum
    print("Part 2 solution: %d" %increased)
