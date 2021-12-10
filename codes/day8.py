import sys

if len(sys.argv) != 2:
	print("python %s <input_file>"  %sys.argv[0])
	sys.exit(0)


uniq_comb = {6:[0, 6, 9], 2:[1], 5: [2, 5, 3], 4:[4], 3: [7], 7:[8]}
uniq_num = [k for k,v in uniq_comb.items() if len(v) == 1]
with open(sys.argv[1], "r") as day8_file:
    lines = day8_file.readlines()

    uniq_count = 0
    for line in lines:
        for word in line.split("|")[1].split(" "):
            if len(word.strip()) in uniq_num:
                uniq_count+=1

    print("Part 1 solution: %d" %uniq_count)


def get_num_letter_map(line):
    num_letter_map = {1:None, 2:None, 3:None, 4:None, 5:None, 6:None, 7:None, 8:None, 9:None}
    while None in num_letter_map.values():
        for word in line.split("|")[0].split(" "):
            if len(word.strip()) in uniq_num:
                num_letter_map[uniq_comb[len(word.strip())][0]] = word.strip()

        for word in line.split("|")[0].split(" "):
            word_len = len(word.strip())
            #Going for 9
            if word_len == 6 and len(set(word.strip()).symmetric_difference(num_letter_map[4])) == 2:
                num_letter_map[9] = word

            #Going for 6
            if word_len == 6 and len(set(word.strip()).symmetric_difference(num_letter_map[1])) == 6:
                num_letter_map[6] = word

            #Going for 0
            if word_len == 6 and len(set(word.strip()).symmetric_difference(num_letter_map[1])) == 4 and len(set(word.strip()).symmetric_difference(num_letter_map[4])) == 4:
                num_letter_map[0] = word

            #Going for 2
            if word_len == 5 and len(set(word.strip()).symmetric_difference(num_letter_map[4])) == 5:
                num_letter_map[2] = word

            #Going for 5
            if word_len == 5 and len(set(word.strip()).symmetric_difference(num_letter_map[4])) == 3 and len(set(word.strip()).symmetric_difference(num_letter_map[1])) == 5:
                num_letter_map[5] = word

            #Going for 3
            if word_len == 5 and len(set(word.strip()).symmetric_difference(num_letter_map[1])) == 3 and len(set(word.strip()).symmetric_difference(num_letter_map[4])) == 3:
                num_letter_map[3] = word

    return num_letter_map

output_val = 0
for line in lines:
    num_letter_map = get_num_letter_map(line)
    output_line = line.split("|")[1].strip()
    comb = ''
    for word in output_line.split(" "):
        nums = uniq_comb[len(word.strip())]
        if len(nums) == 1:
            comb += str(nums[0])
        else:
            for num in nums:
                if len(set(word.strip()).symmetric_difference(num_letter_map[int(num)])) == 0:
                    comb += str(num)
                    break

    print(comb)
    output_val += int(comb)

print("Part 2 solution: %d" %output_val)
