import sys

if len(sys.argv) != 2:
    print("python %s <input_file>" %sys.argv[0])
    sys.exit(0)


import numpy as np

with open(sys.argv[1], "r") as day3_file:
    bits = day3_file.readlines()
    bit_bits = [[b for b in bit.strip()] for bit in bits]

    np_bb_t = np.transpose(bit_bits)

    gamma, epsilon = "", ""
    for reverse_bits in np_bb_t.tolist():
        gamma += max(reverse_bits, key=reverse_bits.count)
        epsilon += min(reverse_bits, key=reverse_bits.count)

    print("Part 1 solution: %d" %((int(gamma, 2)* int(epsilon, 2))))

    oxygen_gen, co2_gen = bits, bits

    np_bb_t = np.transpose([[b for b in bit.strip()] for bit in bits]).tolist()
    bit_index, transpose_pos = 0, 0
    while len(oxygen_gen) > 1:
        reverse_bits = np_bb_t[transpose_pos]
        reverse_bits.sort(reverse=True)
        oxygen = max(reverse_bits, key=reverse_bits.count)
        oxygen_gen = [bit.strip() for bit in oxygen_gen if bit[bit_index].startswith(oxygen)]

        np_bb_t = np.transpose([[b for b in bit.strip()] for bit in oxygen_gen]).tolist()
        bit_index += 1
        transpose_pos += 1

    np_bb_t = np.transpose([[b for b in bit.strip()] for bit in bits]).tolist()
    bit_index, transpose_pos = 0, 0
    while len(co2_gen) > 1:
        reverse_bits = np_bb_t[transpose_pos]
        reverse_bits.sort()
        co2 = min(reverse_bits, key=reverse_bits.count)
        co2_gen = [bit.strip() for bit in co2_gen if bit[bit_index].startswith(co2)]

        np_bb_t = np.transpose([[b for b in bit.strip()] for bit in co2_gen]).tolist()
        bit_index += 1
        transpose_pos += 1

    print("Part 2 solution: %d" %(int(oxygen_gen[0], 2) * int(co2_gen[0], 2)))

