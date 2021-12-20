import sys
import numpy as np

if len(sys.argv) != 2:
    print("python %s <input_file>" %sys.argv[0])
    sys.exit(0)

def bingo(boards, draws, win_pos = "first"):
    if win_pos == "first":
        for draw in draws:
            for i, board in enumerate(boards):
                board[board == draw] = -1
                boards[i] = board

                if np.all(boards[i][0, :] == -1)  or np.all(boards[i][1, :] == -1) or np.all(boards[i][2,:] == -1) or np.all(boards[i][3,:] == -1) or np.all(boards[i][4,:] == -1) or np.all(boards[i][:, 0] == -1) or np.all(boards[i][:, 1] == -1) or np.all(boards[i][:, 2] == -1) or np.all(boards[i][:, 3] == -1) or np.all(boards[i][:,4] == -1):
                    return board, draw

    else:
        ignore_board = []
        for draw in draws:
            for i, board in enumerate(boards):
                if i in ignore_board: continue
                board[board == draw] = -1
                boards[i] = board

                if np.all(boards[i][0, :] == -1)  or np.all(boards[i][1, :] == -1) or np.all(boards[i][2,:] == -1) or np.all(boards[i][3,:] == -1) or np.all(boards[i][4,:] == -1) or np.all(boards[i][:, 0] == -1) or np.all(boards[i][:, 1] == -1) or np.all(boards[i][:, 2] == -1) or np.all(boards[i][:, 3] == -1) or np.all(boards[i][:,4] == -1):
                    ignore_board.append(i)
                i += 1
            if len(ignore_board) + 1 == len(boards):
                break

        
        
        last_board = list(filter(lambda x: x[0] not in ignore_board, enumerate(boards)))[0][1]
        for draw in draws:
            last_board[last_board == draw] = -1
            
            if np.all(last_board[0, :] == -1)  or np.all(last_board[1, :] == -1) or np.all(last_board[2,:] == -1) or np.all(last_board[3,:] == -1) or np.all(last_board[4,:] == -1) or np.all(last_board[:, 0] == -1) or np.all(last_board[:, 1] == -1) or np.all(last_board[:, 2] == -1) or np.all(last_board[:, 3] == -1) or np.all(last_board[:,4] == -1):
                return last_board, draw

            
with open(sys.argv[1], "r") as day4_file:
    boards, draws, current_board, current_index = [], [], [], 0

    for i, line in enumerate(day4_file.readlines()):
        if not line.strip(): continue

        if i == 0:
            draws = map(int, line.strip().split(","))
            p2_draws = map(int, line.strip().split(","))

        else:
            current_board.append(list(map(int, filter(lambda x: x != "" , line.strip().split(' ')))))
            current_index += 1


        if len(current_board) == 5:
            boards.append(np.array(current_board))

            current_board = []
            current_index = 0

    bingo_p1 = bingo(boards, draws)
    print("Part 1 solution: %d" %(np.sum(bingo_p1[0][bingo_p1[0] != -1]) * bingo_p1[1]))

    bingo_p2 = bingo(boards, list(p2_draws), "last")
    print("Part 2 solution: %d" %(np.sum(bingo_p2[0][bingo_p2[0] != -1]) * bingo_p2[1]))
