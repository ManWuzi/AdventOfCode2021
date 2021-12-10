import sys

if len(sys.argv) != 2:
    print('python %s <input_file>' %sys.argv[0])
    sys.exit(0)

with open(sys.argv[1], "r") as day7_file:
    numbers = map(int, day7_file.readline().split(","))

    curr_position, min_fuel, curr_fuel = 0, 0, 0
    while curr_position <= max(numbers):
        curr_fuel = sum(map(lambda x: abs(x-curr_position), numbers))
        if curr_fuel < min_fuel or min_fuel == 0:
            min_fuel = curr_fuel
        curr_position += 1

    print("Part 1 solution: %d" %min_fuel)


    curr_position, min_fuel, curr_fuel = 0, 0, 0
    while curr_position <= max(numbers):
        curr_fuel = sum(map(lambda x: sum(range(1, abs(x-curr_position)+1)), numbers))

        if curr_fuel < min_fuel or min_fuel == 0:
            min_fuel = curr_fuel
        curr_position += 1

    print("Part 2 solution: %d" %min_fuel)
