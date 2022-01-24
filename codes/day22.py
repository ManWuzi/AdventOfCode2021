import sys, copy
import numpy as np


if len(sys.argv) != 2:
    print("python %s <input> " %sys.argv[0])
    sys.exit(0)

def get_cubes(line):
    cubes = line[2:].split(",")
    x = cubes[0].split("=")[1].split("..")
    y = cubes[1].split("=")[1].split("..")
    z = cubes[2].split("=")[1].split("..")

    if int(x[0]) < -50 or int(x[1]) > 50 or int(y[0]) < -50 or int(y[1]) > 50 or int(z[0]) < -50 or int(z[1]) > 50: return None 
        
    return range(int(x[0]), int(x[1])+1), range(int(y[0]), int(y[1])+1), range(int(z[0]), int(z[1])+1)

def diff_lists(a1, a2):
    a1_rows = a1.view([('', a1.dtype)] * a1.shape[1])
    a2_rows = a2.view([('', a2.dtype)] * a2.shape[1])

    return np.setdiff1d(a1_rows, a2_rows).view(a1.dtype).reshape(-1, a1.shape[1])

with open(sys.argv[1], "r") as day22_file:
    lit_cubes = np.array([])
    for line in day22_file.readlines():
        if line.startswith("on"):
            cubes = get_cubes(line)
            if cubes is None: continue
            if lit_cubes.size == 0:
                lit_cubes = np.array(np.meshgrid(cubes[0], cubes[1], cubes[2])).T.reshape(-1, 3)
            else:
                lit_cubes = np.concatenate((np.array(np.meshgrid(cubes[0], cubes[1], cubes[2])).T.reshape(-1, 3), lit_cubes), axis=0)

        elif line.startswith("off"):
            cubes = get_cubes(line)
            if cubes is None: continue
            off_lights = np.array(np.meshgrid(cubes[0], cubes[1], cubes[2])).T.reshape(-1, 3)
            lit_cubes = diff_lists(lit_cubes, off_lights)
        lit_cubes = np.unique(lit_cubes, axis=0)
    # lit_cubes = lit_cubes[np.where((lit_cubes > -50) & (lit_cubes < 50))]
    print("Part 1 solution: %d" %lit_cubes.shape[0])