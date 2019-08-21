#!/usr/bin/env python

# TODO: tail-recursion
# TODO: memoization

NBITS = 8
ADDER_SIZE = 3

def rec_nxor_sat(byte_pos, depth):
    if depth == 0:
        return [[]]
    elif byte_pos == NBITS - 1 or depth == 1:
        return [["a[{}]".format(byte_pos)], ["b[{}]".format(byte_pos)]]
    else:
        sub_lists = rec_nxor_sat(byte_pos+1, depth-1)
        return [["a[{}]".format(byte_pos), "b[{}]".format(byte_pos)]]  \
            + map(lambda x: ["a[{}]".format(byte_pos)] + x, sub_lists) \
            + map(lambda x: ["b[{}]".format(byte_pos)] + x, sub_lists)

def rec_xor_sat(byte_pos, depth):
    if depth == 0:
        return []
    elif byte_pos == NBITS - 1 or depth == 1:
        return [["not a[{}]".format(byte_pos), "not b[{}]".format(byte_pos)]]
    else:
        sub_lists = rec_xor_sat(byte_pos+1, depth-1)
        return [["not a[{}]".format(byte_pos), "not b[{}]".format(byte_pos)]]  \
            + map(lambda x: ["a[{}]".format(byte_pos), "not b[{}]".format(byte_pos)] + x, sub_lists) \
            + map(lambda x: ["not a[{}]".format(byte_pos), "b[{}]".format(byte_pos)] + x, sub_lists)

def sat_add_bit(byte_pos, depth):
    assert 0 <= byte_pos < NBITS, "error byte_pos arg"
    assert 0 < depth <= NBITS, "error byte_pos arg"
    depth = depth - 1
    if byte_pos < NBITS - 1:
        sub_xor_sat = rec_xor_sat(byte_pos + 1, depth)
        sub_nxor_sat = rec_nxor_sat(byte_pos + 1, depth)
        clauses  = map(lambda x: ["a[{}]".format(byte_pos), "b[{}]".format(byte_pos)] + x, sub_nxor_sat)
        clauses += map(lambda x: ["not a[{}]".format(byte_pos), "b[{}]".format(byte_pos)] + x, sub_xor_sat)
        clauses += map(lambda x: ["a[{}]".format(byte_pos), "not b[{}]".format(byte_pos)] + x, sub_xor_sat)
        clauses += map(lambda x: ["not a[{}]".format(byte_pos), "not b[{}]".format(byte_pos)] + x, sub_nxor_sat)
    else:
        clauses = [["a[{}]".format(byte_pos), "b[{}]".format(byte_pos)], ["not a[{}]".format(byte_pos), "not b[{}]".format(byte_pos)]]
    return "\t\t" + "\n\t\tand ".join("(" + " or ".join(c) + ")" for c in clauses)


print "def bool_addition(a, b):"
print "\treturn ["
for bit in range(NBITS):
    print sat_add_bit(bit,ADDER_SIZE) + (", \n" if bit < NBITS - 1 else "")
print "\t]"

""" TESTS

def bool_to_int(a):
    return int(''.join(['1' if b else '0' for b in a]), 2)

def int_to_bool(a, base):
    return [True if b == '1' else False for b in format(a, '0{}b'.format(base))]

success_count = 0
for a in range(2**NBITS):
    for b in range(2**NBITS):
        integer_a_b = (a+b) % 2**NBITS
        bool32_a_b = bool_to_int(bool_addition(int_to_bool(a), int_to_bool(b)))
        #assert integer_a_b == bool32_a_b, str(integer_a_b) + " <> " + str(bool32_a_b) + " ( " + str(a) + " + " + str(b) + " ) "
        if integer_a_b == bool32_a_b:
            success_count += 1
print "{} / {}".format(success_count, 4**NBITS)
"""
