import sys
import numpy as np

if len(sys.argv) != 2:
    print("python %s <input> " %sys.argv[0])
    sys.exit(0)


def fold_algo(arr, fold_instructions):
    if fold_instructions[0] == 'y':
        arr_p1 = np.zeros(shape=(fold_instructions[1], arr.shape[1]))
        for x,row in enumerate(arr):
            if x == fold_instructions[1]: break
            for y, col in enumerate(row):
                arr_p1[x][y] = max(arr[x][y], arr[arr.shape[0]-x-1][y])

    elif fold_instructions[0] == 'x':
        arr_p1 = np.zeros(shape=(arr.shape[0], fold_instructions[1]))
        for x,row in enumerate(arr):
            for y, col in enumerate(row):
                if y == fold_instructions[1]: break
                arr_p1[x][y] = max(arr[x][y], arr[x][arr.shape[1]-y-1])

    return arr_p1

with open(sys.argv[1], "r") as day13_file:
    instructions = day13_file.readlines()

    dots = [(int(dot.split(",")[0]), int(dot.split(",")[1].strip())) for dot in instructions if  not dot.startswith("fold") and len(dot.strip()) != 0]
    fold_instructions = [(fold.split("=")[0][-1], int(fold.split("=")[1].strip())) for fold in instructions if fold.startswith("fold")]
    max_rows = max(dots, key=lambda x:x[0])[0]
    max_cols = max(dots, key=lambda x:x[1])[1]

    arr = np.zeros(shape=(max_cols+1, max_rows+1))
    for dot in dots:
        arr[dot[1]][dot[0]] = 1

    print("Part 1 solutions: %d" %np.count_nonzero(fold_algo(arr, fold_instructions[0]) == 1))

    for fold_ins in fold_instructions:
        arr = fold_algo(arr, fold_ins)

    np.set_printoptions(linewidth=np.inf)
    print(arr)
    for x in arr:
        for y in x:
            if y == 1:
                print('#', end='')
            else:
                print(".", end='')
        print()
