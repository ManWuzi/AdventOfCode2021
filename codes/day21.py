import sys, copy
import numpy as np

if len(sys.argv) != 2:
    print("python %s <input> " %sys.argv[0])
    sys.exit(0)

with open(sys.argv[1], 'r') as day21_file:
    p1_pos = int(day21_file.readline().split(":")[1].strip())
    p2_pos = int(day21_file.readline().split(":")[1].strip())

    p1_score, p2_score = 0, 0
    current_die, no_of_rolls = 1, 0

    d_dice = range(1, 101)
    while p1_score < 1000 or p2_score < 1000:
        for _ in range(3):
            if current_die == 101:
                current_die = 1
            p1_pos += current_die
            current_die+= 1
        no_of_rolls += 3
        p1_pos = p1_pos if p1_pos <= 10 else p1_pos % 10 
        p1_score += p1_pos
    
        if p1_score > 1000: break 

        for _ in range(3):
            if current_die == 101:
                current_die = 1
            p2_pos += current_die
            current_die+= 1
        no_of_rolls += 3
        p2_pos = p2_pos if p2_pos <= 10 else p2_pos % 10 
        p2_score += p2_pos

        if p2_score > 1000: break

    print("Part 1 solution: %d" %(min(p1_score, p2_score)*no_of_rolls))
    print(no_of_rolls, p1_score, p2_score)
