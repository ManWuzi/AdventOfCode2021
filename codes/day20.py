import sys, copy
import numpy as np

if len(sys.argv) != 2:
    print("python %s <input> " %sys.argv[0])
    sys.exit(0)

def get_adjacent_indices(i, j, arr):
    adjacent_indices = []
    m, n = arr.shape
    for x in range(i-1, i+2):
        for y in range(j-1, j+2):
            if x < 0 or y < 0 or x >= m or y >= n:
                adjacent_indices.append(0)
            else:
                adjacent_indices.append(int(arr[x][y]))
    return adjacent_indices

def surround_image(arr):
    horizontal = np.zeros((arr.shape[0], 1))
    vertical = np.zeros((1, arr.shape[1]))

    arr = np.concatenate((arr, horizontal.T), axis=0)
    arr = np.concatenate((horizontal.T, arr), axis=0)

    vertical = np.zeros((1, arr.shape[0]))
    arr = np.concatenate((vertical.T, arr), axis=1)
    arr = np.concatenate((arr, vertical.T), axis=1)
    return arr
    

with open(sys.argv[1], "r") as day20_file:
    enhancement_algo, image = [], []
    for i, line in enumerate(day20_file.readlines()):
        if not line.strip(): continue
        if i == 0:
            enhancement_algo = list(map(lambda x: 0 if x == "." else 1, list(line.strip())))
        else:
            image.append(list(map(lambda x: 0 if x == "." else 1, list(line.strip()))))
    image = np.array(image)
    for i in range(0,2):
        new_image = np.zeros((image.shape[0], image.shape[1]))
        for r in range(image.shape[0]):
            for c in range(image.shape[1]):
                new_image[r][c] = enhancement_algo[int(''.join(map(str, get_adjacent_indices(r, c, image))), 2)]
        image = copy.deepcopy(new_image)
    print("Part 1 solution: %d" %(np.count_nonzero(image[2:image.shape[0], 2:image.shape[1]] == 1)))