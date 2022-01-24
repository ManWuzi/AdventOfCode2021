import sys
from collections import defaultdict, Counter

if len(sys.argv) != 2:
    print("python %s <input_file>" %sys.argv[1])
    sys.exit(0)

def get_link_p1(paths, curr_cave, links, curr_path):
    for link in links[curr_cave]:
        if link.islower() and link in curr_path:
            continue
        else:
            paths = get_link_p1(paths, link, links, curr_path+[link])
            if curr_path not in paths: paths.append(curr_path)
    return paths

def get_link_p2(paths, curr_cave, links, curr_path):
    for link in links[curr_cave]:
        if link.islower() and link in curr_path:
            if link == "start" or link == "end" or 2 in Counter(filter(lambda x: x.islower(), curr_path)).values():
                continue
        paths = get_link_p2(paths, link, links, curr_path+[link])
        if curr_path not in paths and "end" == curr_path[-1]: paths.append(curr_path)
    return paths



with open(sys.argv[1], "r") as day12_file:
    cave_map = day12_file.readlines()
    cave_links = defaultdict(list)
    for cave_con in cave_map:
        a, b = cave_con.split("-")[0], cave_con.split("-")[1].strip()
        cave_links[a].append(b)
        cave_links[b].append(a)

    paths = get_link_p1([], "start", cave_links, ["start"])
    paths = list(filter(lambda path: path[-1] == "end", paths))

    print("Part 1 solution: %d" %len(paths))


    paths = get_link_p2([], "start", cave_links, ['start'])
    paths = list(filter(lambda path: path[-1] == "end", paths))

    print("Part 2 solution: %d" %len(paths))
