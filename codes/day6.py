import sys, copy
from collections import Counter

if len(sys.argv) != 2:
    print("python %s <input> " %sys.argv[0])
    sys.exit(0)

def spawn_lantern(fish):
    if fish == 0:
        return 6
    return fish-1

def create_lantern(days, timer):
    timer = [timer]
    for i in range(len(timer)):
        if timer[i] == 0:
            timer[i] = 6
            timer.append(8)
        else:
            timer[i] = timer[i] -1
    return len(timer)**days

with open(sys.argv[1], "r") as day6_file:
    lantern_fish = map(int, day6_file.readline().split(","))
    p2_lantern_fish = copy.deepcopy(lantern_fish)

    day = 0
    old_lantern_fish = lantern_fish
    while day < 80:
        lantern_fish = list(map(spawn_lantern, lantern_fish))
        lantern_fish += [8] * len(list(filter(lambda x: x==0, old_lantern_fish)))
        old_lantern_fish = lantern_fish
        day += 1

    print("Part 1 solution: %d" %len(lantern_fish))

    p2_lantern_fish = Counter(p2_lantern_fish)
    
    old_p2_lantern_fish = copy.deepcopy(p2_lantern_fish)
    day, zf = 0, 0
    while day < 256:
        for k in range(8, -1, -1):
            if k == 0:
                zf = old_p2_lantern_fish[k]
                p2_lantern_fish[6] += old_p2_lantern_fish[k]
                continue
            p2_lantern_fish[k-1] = old_p2_lantern_fish[k]

        p2_lantern_fish[8] = zf
        old_p2_lantern_fish = copy.deepcopy(p2_lantern_fish)

        zf = 0
        day+=1

    print("Part 2 solution: %d" %sum(p2_lantern_fish.values()))