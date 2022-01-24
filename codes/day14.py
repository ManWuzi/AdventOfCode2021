import sys
from collections import Counter, defaultdict

if len(sys.argv) != 2:
    print("python %s <input>" %sys.argv[0])
    sys.exit(0)

with open(sys.argv[1], "r") as day14_file:
    template, insertions = "", {}
    for line in day14_file.readlines():
        line  = line.strip()
        if not line: continue
        if "->" in line:
            pair = line.split("->")[0].strip()
            element = line.split("->")[1].strip()

            insertions[pair] = element
        else:
            template = line.strip()

    for i in range(10):
        element_insertions = []
        for i in range(len(template)):
            if template[i:i+2] in insertions.keys():
                element_insertions.append((insertions[template[i:i+2]], i))
        for i, ei in enumerate(element_insertions):
            template = template[:ei[1]+1+i] + ei[0] + template[ei[1]+i+1:]

    template_counter = Counter(list(template))
    print("Part 1 solutions: %d" %(max(template_counter.values())-min(template_counter.values())))

    pairs = defaultdict(int)
    for i in range(len(template)):
        pairs[template[i:i+2]] = pairs[template[i:i+2]]+1

    for i in range(10):
        eis = filter(lambda x: x in insertions.keys(), pairs.keys())
        for j in eis:
            element = insertions[j]
            pairs[j[0] + element] = pairs[j[0] + element] + 1
            pairs[element + j[1]] = pairs[element + j[1]] + 1

    letter_values = defaultdict(int)
    for k,v in pairs.items():
        letter_values[k[0]] = letter_values[k[0]] + v

        if len(k) >1: letter_values[k[1]] = letter_values[k[1]] + v

    print("Part 2 solutions: %d" %(max(letter_values.values()) - min(letter_values.values())))


