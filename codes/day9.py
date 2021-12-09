import sys
import numpy as np

if len(sys.argv) != 2:
    print("python %s <input_file> " %sys.argv[0])
    sys.exit(0)

with open(sys.argv[1], "r") as day9_file:
    line = day9_file.readlines()
    np_heights = np.array([[int(h.strip()) for h in heights.strip()] for heights in line])

risk_level = 0
for iy, ix in np.ndindex(np_heights.shape):
    low_point, up, down, left, right = np_heights[iy, ix], np_heights[iy+1, ix] if np_heights.shape[0] > iy+1    else 10, np_heights[iy-1, ix] if iy-1 >= 0  else 10, np_heights[iy, ix-1] if ix-1 >= 0  else 10, np_heights[iy, ix+1] if np_heights.shape[1] > ix+1  else 10
    if low_point < up and low_point < down and low_point < left and low_point < right:
        risk_level += low_point+1

print("Part 1 solution: %d" %risk_level)

def basin_size(np_heights, iy, ix, visited_p):
    # Left flow
    lf_i = ix-1
    while lf_i >=0 and np_heights[iy, lf_i] != 9:
        if [iy, lf_i] in visited_p: break
        visited_p.append([iy, lf_i])
        visited_p = basin_size(np_heights, iy, lf_i, visited_p)
        lf_i -= 1
    # Right flow
    rf_i = ix+1
    while rf_i < np_heights.shape[1] and np_heights[iy, rf_i] !=9:
        if [iy, rf_i] in visited_p: break
        visited_p.append([iy, rf_i])
        visited_p = basin_size(np_heights, iy, rf_i, visited_p)
        rf_i += 1
    # Up flow
    uf_i = iy-1
    while uf_i >=0 and np_heights[uf_i, ix] != 9:
        if [uf_i, ix] in visited_p: break
        visited_p.append([uf_i, ix])
        visited_p = basin_size(np_heights, uf_i, ix, visited_p)
        uf_i -=1
    # Down flow
    df_i = iy+1
    while df_i < np_heights.shape[0] and np_heights[df_i, ix] != 9:
        if [df_i, ix] in visited_p: break
        visited_p.append([df_i, ix])
        visited_p = basin_size(np_heights, df_i, ix, visited_p)
        df_i += 1
    return visited_p


all_basin_sizes = []
for iy, ix in np.ndindex(np_heights.shape):
    low_point, up, down, left, right = np_heights[iy, ix], np_heights[iy+1, ix] if np_heights.shape[0] > iy+1    else 10, np_heights[iy-1, ix] if iy-1 >= 0  else 10, np_heights[iy, ix-1] if ix-1 >= 0  else 10, np_heights[iy, ix+1] if np_heights.shape[1] > ix+1  else 10
    if low_point < up and low_point < down and low_point < left and low_point < right:
        visited_p= basin_size(np_heights, iy, ix, [iy,ix])
        all_basin_sizes.append(len(visited_p[2:]))

all_basin_sizes.sort(reverse=True)
print("Part 2 solution: %d" %np.product(all_basin_sizes[:3]))
