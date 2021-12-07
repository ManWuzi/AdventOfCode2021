import sys

if len(sys.argv) != 2:
    print("python %s [input_file]" %sys.argv[0])
    sys.exit(0)


with open(sys.argv[1], "r") as day2_file:
    horizontal, depth = 0, 0
    lines = day2_file.readlines()
    for line in lines:
        instruction, value = line.split()[0], int(line.split()[1])
        if instruction == "forward":
            horizontal += value
        elif instruction == "down":
            depth += value
        elif instruction == "up":
            depth -= value

    print("Part 1 solution: %d" %(horizontal*depth))

    horizontal, depth, aim = 0, 0, 0
    for line in lines:
        instruction, value = line.split()[0], int(line.split()[1])
        if instruction == "forward":
            horizontal += value
            depth = depth + (value * aim)
        elif instruction == "down":
            aim += value
        elif instruction == "up":
            aim -= value

    print("Part 2 solution: %d" %(horizontal*depth))
