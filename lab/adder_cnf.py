#!/usr/bin/env python

NBITS = 8

# TODO: tail-recursion
# TODO: memoization

def rec_nxor_sat(byte_pos):
    if byte_pos == NBITS - 1:
        return [["a[{}]".format(byte_pos)], ["b[{}]".format(byte_pos)]]
    else:
        sub_lists = rec_nxor_sat(byte_pos+1)
        return [["a[{}]".format(byte_pos), "b[{}]".format(byte_pos)]]  \
            + map(lambda x: ["a[{}]".format(byte_pos)] + x, sub_lists) \
            + map(lambda x: ["b[{}]".format(byte_pos)] + x, sub_lists)

def rec_xor_sat(byte_pos):
    if byte_pos == NBITS - 1:
        return [["not a[{}]".format(byte_pos), "not b[{}]".format(byte_pos)]]
    else:
        sub_lists = rec_xor_sat(byte_pos+1)
        return [["not a[{}]".format(byte_pos), "not b[{}]".format(byte_pos)]]  \
            + map(lambda x: ["a[{}]".format(byte_pos)] + x, sub_lists) \
            + map(lambda x: ["b[{}]".format(byte_pos)] + x, sub_lists)

def sat_add_bit(byte_pos):
    assert 0 <= byte_pos < NBITS, "error byte_pos arg"
    if byte_pos < NBITS - 1:
        sub_xor_sat = rec_xor_sat(byte_pos + 1)
        sub_nxor_sat = rec_nxor_sat(byte_pos + 1)
        clauses  = map(lambda x: ["a[{}]".format(byte_pos), "b[{}]".format(byte_pos)] + x, sub_nxor_sat)
        clauses += map(lambda x: ["not a[{}]".format(byte_pos), "b[{}]".format(byte_pos)] + x, sub_xor_sat)
        clauses += map(lambda x: ["a[{}]".format(byte_pos), "not b[{}]".format(byte_pos)] + x, sub_xor_sat)
        clauses += map(lambda x: ["not a[{}]".format(byte_pos), "not b[{}]".format(byte_pos)] + x, sub_nxor_sat)
    else:
        clauses = [["a[{}]".format(byte_pos), "b[{}]".format(byte_pos)], ["not a[{}]".format(byte_pos), "not b[{}]".format(byte_pos)]]
    return "\t\t" + "\n\t\tand ".join("(" + " or ".join(c) + ")" for c in clauses)


print "def bool32_addition(a, b):"
print "\treturn ["
for bit in range(NBITS):
    print sat_add_bit(bit) + (", \n" if bit < NBITS - 1 else "")
print "\t]"
