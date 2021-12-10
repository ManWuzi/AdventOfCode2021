import sys
from collections import Counter

if len(sys.argv) != 2:
    print("python %s <input_file> " %sys.argv[0])
    sys.exit(0)

illegal_score = {")": 3, "]": 57, "}": 1197, ">": 25137}
illegals = []

complete_score = {")": 1, "]": 2, "}": 3, ">": 4}

def get_illegal_char(line):
    chunks = list(line.strip())
    chunk_i = 0
    while chunk_i < len(chunks):
        if chunks[chunk_i] in illegal_score.keys():
            if chunks[chunk_i-1] + chunks[chunk_i] in ["{}", "[]", "<>", "()"]:
                del chunks[chunk_i]
                del chunks[chunk_i-1]
                chunk_i = 0
                continue
            else:
                return chunks, chunks[chunk_i]
        chunk_i += 1
    return chunks, None

with open(sys.argv[1], "r") as day10_file:
    lines = day10_file.readlines()
    for line in lines:
        _, illegal = get_illegal_char(line)
        if illegal is not None:
            illegals.append(illegal)

    total_illegal = 0
    for k, v in Counter(illegals).items():
        total_illegal += illegal_score[k] * v

    print("Part 1 solution: %d" %total_illegal)


    all_scores = []
    for line in lines:
        chunks, illegal = get_illegal_char(line)
        if illegal is not None: continue

        chunk_end = ""
        total_score = 0
        for chunk in chunks[::-1]:
            total_score *= 5
            if chunk == "{":
                total_score += complete_score["}"]
            elif chunk == "[":
                total_score += complete_score["]"]
            elif chunk == "<":
                total_score += complete_score[">"]
            elif chunk == "(":
                total_score += complete_score[")"]
        all_scores.append(total_score)

    all_scores.sort()
    print("Part 2 solution: %d" %all_scores[len(all_scores)/2])

