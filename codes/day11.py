import sys
import numpy as np
import copy

if len(sys.argv) != 2:
    print("python %s <input_file>" %sys.argv[0])
    sys.exit(0)

def get_adjacent_indices(i, j, arr):
    adjacent_indices = []
    m, n = arr.shape
    if i > 0: #left
        adjacent_indices.append((i-1, j))
    if i+1 < m: #right
        adjacent_indices.append((i+1, j))
    if j > 0: #up
        adjacent_indices.append((i, j-1))
    if j+1 < n: #down
        adjacent_indices.append((i, j+1))
    if i > 0 and j > 0: #up-left
        adjacent_indices.append((i-1, j-1))
    if i+1 < m and j > 0: #up-right
        adjacent_indices.append((i+1, j-1))
    if i > 0 and j+1 < n: #down-left
        adjacent_indices.append((i-1, j+1))
    if i+1 < m and j+1 < n: #down-right
        adjacent_indices.append((i+1, j+1))
    return adjacent_indices

with open(sys.argv[1], "r") as day11_file:
    oct_en_levels = np.array([[int(col.strip()) for col in row if len(col.strip()) == 1] for row in day11_file.readlines()])

    step, flash, checked = 10, 0, []
    while step > 0:
        print(oct_en_levels)
        oct_en_levels += 1
        
        over_9 = [(i,j) for i, j in zip(np.where(oct_en_levels > 9)[0], np.where(oct_en_levels > 9)[1])]

        while len(over_9) > 0:
            i, j = over_9.pop()
            if (i, j) in checked: continue

            ai_s = get_adjacent_indices(i, j, oct_en_levels)
            for ai in ai_s:
                oct_en_levels[ai[0]][ai[1]] += 1
                
            checked.append((i,j))
            over_9 = [(i,j) for i, j in zip(np.where(oct_en_levels > 9)[0], np.where(oct_en_levels > 9)[1])]

        over_9 = [(i,j) for i, j in zip(np.where(oct_en_levels > 9)[0], np.where(oct_en_levels > 9)[1])]
        flash += len(over_9)
        for x, y in over_9:
            oct_en_levels[x][y] = 0

        step -= 1
    print("Part 1 solution: %d" %flash)