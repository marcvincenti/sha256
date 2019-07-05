#!/usr/bin/env python

import hashlib

initial_bool_values=[
    False, True, True, False, True, False, True, False, False, False, False, False, True, False, False, True, True, True, True, False, False, True, True, False, False, True, True, False, False, True, True, True,
    True, False, True, True, True, False, True, True, False, True, True, False, False, True, True, True, True, False, True, False, True, True, True, False, True, False, False, False, False, True, False, True,
    False, False, True, True, True, True, False, False, False, True, True, False, True, True, True, False, True, True, True, True, False, False, True, True, False, True, True, True, False, False, True, False,
    True, False, True, False, False, True, False, True, False, True, False, False, True, True, True, True, True, True, True, True, False, True, False, True, False, False, True, True, True, False, True, False,
    False, True, False, True, False, False, False, True, False, False, False, False, True, True, True, False, False, True, False, True, False, False, True, False, False, True, True, True, True, True, True, True,
    True, False, False, True, True, False, True, True, False, False, False, False, False, True, False, True, False, True, True, False, True, False, False, False, True, False, False, False, True, True, False, False,
    False, False, False, True, True, True, True, True, True, False, False, False, False, False, True, True, True, True, False, True, True, False, False, True, True, False, True, False, True, False, True, True,
    False, True, False, True, True, False, True, True, True, True, True, False, False, False, False, False, True, True, False, False, True, True, False, True, False, False, False, True, True, False, False, True
]

sha_bool_constants = [
    [False, True, False, False, False, False, True, False, True, False, False, False, True, False, True, False, False, False, True, False, True, True, True, True, True, False, False, True, True, False, False, False],
    [False, True, True, True, False, False, False, True, False, False, True, True, False, True, True, True, False, True, False, False, False, True, False, False, True, False, False, True, False, False, False, True],
    [True, False, True, True, False, True, False, True, True, True, False, False, False, False, False, False, True, True, True, True, True, False, True, True, True, True, False, False, True, True, True, True],
    [True, True, True, False, True, False, False, True, True, False, True, True, False, True, False, True, True, True, False, True, True, False, True, True, True, False, True, False, False, True, False, True],
    [False, False, True, True, True, False, False, True, False, True, False, True, False, True, True, False, True, True, False, False, False, False, True, False, False, True, False, True, True, False, True, True],
    [False, True, False, True, True, False, False, True, True, True, True, True, False, False, False, True, False, False, False, True, False, False, False, True, True, True, True, True, False, False, False, True],
    [True, False, False, True, False, False, True, False, False, False, True, True, True, True, True, True, True, False, False, False, False, False, True, False, True, False, True, False, False, True, False, False],
    [True, False, True, False, True, False, True, True, False, False, False, True, True, True, False, False, False, True, False, True, True, True, True, False, True, True, False, True, False, True, False, True],
    [True, True, False, True, True, False, False, False, False, False, False, False, False, True, True, True, True, False, True, False, True, False, True, False, True, False, False, True, True, False, False, False],
    [False, False, False, True, False, False, True, False, True, False, False, False, False, False, True, True, False, True, False, True, True, False, True, True, False, False, False, False, False, False, False, True],
    [False, False, True, False, False, True, False, False, False, False, True, True, False, False, False, True, True, False, False, False, False, True, False, True, True, False, True, True, True, True, True, False],
    [False, True, False, True, False, True, False, True, False, False, False, False, True, True, False, False, False, True, True, True, True, True, False, True, True, True, False, False, False, False, True, True],
    [False, True, True, True, False, False, True, False, True, False, True, True, True, True, True, False, False, True, False, True, True, True, False, True, False, True, True, True, False, True, False, False],
    [True, False, False, False, False, False, False, False, True, True, False, True, True, True, True, False, True, False, True, True, False, False, False, True, True, True, True, True, True, True, True, False],
    [True, False, False, True, True, False, True, True, True, True, False, True, True, True, False, False, False, False, False, False, False, True, True, False, True, False, True, False, False, True, True, True],
    [True, True, False, False, False, False, False, True, True, False, False, True, True, False, True, True, True, True, True, True, False, False, False, True, False, True, True, True, False, True, False, False],
    [True, True, True, False, False, True, False, False, True, False, False, True, True, False, True, True, False, True, True, False, True, False, False, True, True, True, False, False, False, False, False, True],
    [True, True, True, False, True, True, True, True, True, False, True, True, True, True, True, False, False, True, False, False, False, True, True, True, True, False, False, False, False, True, True, False],
    [False, False, False, False, True, True, True, True, True, True, False, False, False, False, False, True, True, False, False, True, True, True, False, True, True, True, False, False, False, True, True, False],
    [False, False, True, False, False, True, False, False, False, False, False, False, True, True, False, False, True, False, True, False, False, False, False, True, True, True, False, False, True, True, False, False],
    [False, False, True, False, True, True, False, True, True, True, True, False, True, False, False, True, False, False, True, False, True, True, False, False, False, True, True, False, True, True, True, True],
    [False, True, False, False, True, False, True, False, False, True, True, True, False, True, False, False, True, False, False, False, False, True, False, False, True, False, True, False, True, False, True, False],
    [False, True, False, True, True, True, False, False, True, False, True, True, False, False, False, False, True, False, True, False, True, False, False, True, True, True, False, True, True, True, False, False],
    [False, True, True, True, False, True, True, False, True, True, True, True, True, False, False, True, True, False, False, False, True, False, False, False, True, True, False, True, True, False, True, False],
    [True, False, False, True, True, False, False, False, False, False, True, True, True, True, True, False, False, True, False, True, False, False, False, True, False, True, False, True, False, False, True, False],
    [True, False, True, False, True, False, False, False, False, False, True, True, False, False, False, True, True, True, False, False, False, True, True, False, False, True, True, False, True, True, False, True],
    [True, False, True, True, False, False, False, False, False, False, False, False, False, False, True, True, False, False, True, False, False, True, True, True, True, True, False, False, True, False, False, False],
    [True, False, True, True, True, True, True, True, False, True, False, True, True, False, False, True, False, True, True, True, True, True, True, True, True, True, False, False, False, True, True, True],
    [True, True, False, False, False, True, True, False, True, True, True, False, False, False, False, False, False, False, False, False, True, False, True, True, True, True, True, True, False, False, True, True],
    [True, True, False, True, False, True, False, True, True, False, True, False, False, True, True, True, True, False, False, True, False, False, False, True, False, True, False, False, False, True, True, True],
    [False, False, False, False, False, True, True, False, True, True, False, False, True, False, True, False, False, True, True, False, False, False, True, True, False, True, False, True, False, False, False, True],
    [False, False, False, True, False, True, False, False, False, False, True, False, True, False, False, True, False, False, True, False, True, False, False, True, False, True, True, False, False, True, True, True],
    [False, False, True, False, False, True, True, True, True, False, True, True, False, True, True, True, False, False, False, False, True, False, True, False, True, False, False, False, False, True, False, True],
    [False, False, True, False, True, True, True, False, False, False, False, True, True, False, True, True, False, False, True, False, False, False, False, True, False, False, True, True, True, False, False, False],
    [False, True, False, False, True, True, False, True, False, False, True, False, True, True, False, False, False, True, True, False, True, True, False, True, True, True, True, True, True, True, False, False],
    [False, True, False, True, False, False, True, True, False, False, True, True, True, False, False, False, False, False, False, False, True, True, False, True, False, False, False, True, False, False, True, True],
    [False, True, True, False, False, True, False, True, False, False, False, False, True, False, True, False, False, True, True, True, False, False, True, True, False, True, False, True, False, True, False, False],
    [False, True, True, True, False, True, True, False, False, True, True, False, True, False, True, False, False, False, False, False, True, False, True, False, True, False, True, True, True, False, True, True],
    [True, False, False, False, False, False, False, True, True, True, False, False, False, False, True, False, True, True, False, False, True, False, False, True, False, False, True, False, True, True, True, False],
    [True, False, False, True, False, False, True, False, False, True, True, True, False, False, True, False, False, False, True, False, True, True, False, False, True, False, False, False, False, True, False, True],
    [True, False, True, False, False, False, True, False, True, False, True, True, True, True, True, True, True, True, True, False, True, False, False, False, True, False, True, False, False, False, False, True],
    [True, False, True, False, True, False, False, False, False, False, False, True, True, False, True, False, False, True, True, False, False, True, True, False, False, True, False, False, True, False, True, True],
    [True, True, False, False, False, False, True, False, False, True, False, False, True, False, True, True, True, False, False, False, True, False, True, True, False, True, True, True, False, False, False, False],
    [True, True, False, False, False, True, True, True, False, True, True, False, True, True, False, False, False, True, False, True, False, False, False, True, True, False, True, False, False, False, True, True],
    [True, True, False, True, False, False, False, True, True, False, False, True, False, False, True, False, True, True, True, False, True, False, False, False, False, False, False, True, True, False, False, True],
    [True, True, False, True, False, True, True, False, True, False, False, True, True, False, False, True, False, False, False, False, False, True, True, False, False, False, True, False, False, True, False, False],
    [True, True, True, True, False, True, False, False, False, False, False, False, True, True, True, False, False, False, True, True, False, True, False, True, True, False, False, False, False, True, False, True],
    [False, False, False, True, False, False, False, False, False, True, True, False, True, False, True, False, True, False, True, False, False, False, False, False, False, True, True, True, False, False, False, False],
    [False, False, False, True, True, False, False, True, True, False, True, False, False, True, False, False, True, True, False, False, False, False, False, True, False, False, False, True, False, True, True, False],
    [False, False, False, True, True, True, True, False, False, False, True, True, False, True, True, True, False, True, True, False, True, True, False, False, False, False, False, False, True, False, False, False],
    [False, False, True, False, False, True, True, True, False, True, False, False, True, False, False, False, False, True, True, True, False, True, True, True, False, True, False, False, True, True, False, False],
    [False, False, True, True, False, True, False, False, True, False, True, True, False, False, False, False, True, False, True, True, True, True, False, False, True, False, True, True, False, True, False, True],
    [False, False, True, True, True, False, False, True, False, False, False, True, True, True, False, False, False, False, False, False, True, True, False, False, True, False, True, True, False, False, True, True],
    [False, True, False, False, True, True, True, False, True, True, False, True, True, False, False, False, True, False, True, False, True, False, True, False, False, True, False, False, True, False, True, False],
    [False, True, False, True, True, False, True, True, True, False, False, True, True, True, False, False, True, True, False, False, True, False, True, False, False, True, False, False, True, True, True, True],
    [False, True, True, False, True, False, False, False, False, False, True, False, True, True, True, False, False, True, True, False, True, True, True, True, True, True, True, True, False, False, True, True],
    [False, True, True, True, False, True, False, False, True, False, False, False, True, True, True, True, True, False, False, False, False, False, True, False, True, True, True, False, True, True, True, False],
    [False, True, True, True, True, False, False, False, True, False, True, False, False, True, False, True, False, True, True, False, False, False, True, True, False, True, True, False, True, True, True, True],
    [True, False, False, False, False, True, False, False, True, True, False, False, True, False, False, False, False, True, True, True, True, False, False, False, False, False, False, True, False, True, False, False],
    [True, False, False, False, True, True, False, False, True, True, False, False, False, True, True, True, False, False, False, False, False, False, True, False, False, False, False, False, True, False, False, False],
    [True, False, False, True, False, False, False, False, True, False, True, True, True, True, True, False, True, True, True, True, True, True, True, True, True, True, True, True, True, False, True, False],
    [True, False, True, False, False, True, False, False, False, True, False, True, False, False, False, False, False, True, True, False, True, True, False, False, True, True, True, False, True, False, True, True],
    [True, False, True, True, True, True, True, False, True, True, True, True, True, False, False, True, True, False, True, False, False, False, True, True, True, True, True, True, False, True, True, True],
    [True, True, False, False, False, True, True, False, False, True, True, True, False, False, False, True, False, True, True, True, True, False, False, False, True, True, True, True, False, False, True, False]
]

def bool_32_addition(a, b):
    r_31 = a[31] and b[31]
    r_30 = (a[30] and b[30]) or (a[30] and r_31) or (b[30] and r_31)
    r_29 = (a[29] and b[29]) or (a[29] and r_30) or (b[29] and r_30)
    r_28 = (a[28] and b[28]) or (a[28] and r_29) or (b[28] and r_29)
    r_27 = (a[27] and b[27]) or (a[27] and r_28) or (b[27] and r_28)
    r_26 = (a[26] and b[26]) or (a[26] and r_27) or (b[26] and r_27)
    r_25 = (a[25] and b[25]) or (a[25] and r_26) or (b[25] and r_26)
    r_24 = (a[24] and b[24]) or (a[24] and r_25) or (b[24] and r_25)
    r_23 = (a[23] and b[23]) or (a[23] and r_24) or (b[23] and r_24)
    r_22 = (a[22] and b[22]) or (a[22] and r_23) or (b[22] and r_23)
    r_21 = (a[21] and b[21]) or (a[21] and r_22) or (b[21] and r_22)
    r_20 = (a[20] and b[20]) or (a[20] and r_21) or (b[20] and r_21)
    r_19 = (a[19] and b[19]) or (a[19] and r_20) or (b[19] and r_20)
    r_18 = (a[18] and b[18]) or (a[18] and r_19) or (b[18] and r_19)
    r_17 = (a[17] and b[17]) or (a[17] and r_18) or (b[17] and r_18)
    r_16 = (a[16] and b[16]) or (a[16] and r_17) or (b[16] and r_17)
    r_15 = (a[15] and b[15]) or (a[15] and r_16) or (b[15] and r_16)
    r_14 = (a[14] and b[14]) or (a[14] and r_15) or (b[14] and r_15)
    r_13 = (a[13] and b[13]) or (a[13] and r_14) or (b[13] and r_14)
    r_12 = (a[12] and b[12]) or (a[12] and r_13) or (b[12] and r_13)
    r_11 = (a[11] and b[11]) or (a[11] and r_12) or (b[11] and r_12)
    r_10 = (a[10] and b[10]) or (a[10] and r_11) or (b[10] and r_11)
    r_9 = (a[9] and b[9]) or (a[9] and r_10) or (b[9] and r_10)
    r_8 = (a[8] and b[8]) or (a[8] and r_9) or (b[8] and r_9)
    r_7 = (a[7] and b[7]) or (a[7] and r_8) or (b[7] and r_8)
    r_6 = (a[6] and b[6]) or (a[6] and r_7) or (b[6] and r_7)
    r_5 = (a[5] and b[5]) or (a[5] and r_6) or (b[5] and r_6)
    r_4 = (a[4] and b[4]) or (a[4] and r_5) or (b[4] and r_5)
    r_3 = (a[3] and b[3]) or (a[3] and r_4) or (b[3] and r_4)
    r_2 = (a[2] and b[2]) or (a[2] and r_3) or (b[2] and r_3)
    r_1 = (a[1] and b[1]) or (a[1] and r_2) or (b[1] and r_2)
    return [
        a[0] ^ b[0] ^ r_1,
        a[1] ^ b[1] ^ r_2,
        a[2] ^ b[2] ^ r_3,
        a[3] ^ b[3] ^ r_4,
        a[4] ^ b[4] ^ r_5,
        a[5] ^ b[5] ^ r_6,
        a[6] ^ b[6] ^ r_7,
        a[7] ^ b[7] ^ r_8,
        a[8] ^ b[8] ^ r_9,
        a[9] ^ b[9] ^ r_10,
        a[10] ^ b[10] ^ r_11,
        a[11] ^ b[11] ^ r_12,
        a[12] ^ b[12] ^ r_13,
        a[13] ^ b[13] ^ r_14,
        a[14] ^ b[14] ^ r_15,
        a[15] ^ b[15] ^ r_16,
        a[16] ^ b[16] ^ r_17,
        a[17] ^ b[17] ^ r_18,
        a[18] ^ b[18] ^ r_19,
        a[19] ^ b[19] ^ r_20,
        a[20] ^ b[20] ^ r_21,
        a[21] ^ b[21] ^ r_22,
        a[22] ^ b[22] ^ r_23,
        a[23] ^ b[23] ^ r_24,
        a[24] ^ b[24] ^ r_25,
        a[25] ^ b[25] ^ r_26,
        a[26] ^ b[26] ^ r_27,
        a[27] ^ b[27] ^ r_28,
        a[28] ^ b[28] ^ r_29,
        a[29] ^ b[29] ^ r_30,
        a[30] ^ b[30] ^ r_31,
        a[31] ^ b[31]
    ]

def bool_e_0(x):
    return [
        (x[30] or x[19] or x[10]) and (x[30] or not x[19] or not x[10]) and (not x[30] or x[19] or not x[10]) and (not x[30] or not x[19] or x[10]),
        (x[31] or x[20] or x[11]) and (x[31] or not x[20] or not x[11]) and (not x[31] or x[20] or not x[11]) and (not x[31] or not x[20] or x[11]),
        (x[0] or x[21] or x[12]) and (x[0] or not x[21] or not x[12]) and (not x[0] or x[21] or not x[12]) and (not x[0] or not x[21] or x[12]),
        (x[1] or x[22] or x[13]) and (x[1] or not x[22] or not x[13]) and (not x[1] or x[22] or not x[13]) and (not x[1] or not x[22] or x[13]),
        (x[2] or x[23] or x[14]) and (x[2] or not x[23] or not x[14]) and (not x[2] or x[23] or not x[14]) and (not x[2] or not x[23] or x[14]),
        (x[3] or x[24] or x[15]) and (x[3] or not x[24] or not x[15]) and (not x[3] or x[24] or not x[15]) and (not x[3] or not x[24] or x[15]),
        (x[4] or x[25] or x[16]) and (x[4] or not x[25] or not x[16]) and (not x[4] or x[25] or not x[16]) and (not x[4] or not x[25] or x[16]),
        (x[5] or x[26] or x[17]) and (x[5] or not x[26] or not x[17]) and (not x[5] or x[26] or not x[17]) and (not x[5] or not x[26] or x[17]),
        (x[6] or x[27] or x[18]) and (x[6] or not x[27] or not x[18]) and (not x[6] or x[27] or not x[18]) and (not x[6] or not x[27] or x[18]),
        (x[7] or x[28] or x[19]) and (x[7] or not x[28] or not x[19]) and (not x[7] or x[28] or not x[19]) and (not x[7] or not x[28] or x[19]),
        (x[8] or x[29] or x[20]) and (x[8] or not x[29] or not x[20]) and (not x[8] or x[29] or not x[20]) and (not x[8] or not x[29] or x[20]),
        (x[9] or x[30] or x[21]) and (x[9] or not x[30] or not x[21]) and (not x[9] or x[30] or not x[21]) and (not x[9] or not x[30] or x[21]),
        (x[10] or x[31] or x[22]) and (x[10] or not x[31] or not x[22]) and (not x[10] or x[31] or not x[22]) and (not x[10] or not x[31] or x[22]),
        (x[11] or x[0] or x[23]) and (x[11] or not x[0] or not x[23]) and (not x[11] or x[0] or not x[23]) and (not x[11] or not x[0] or x[23]),
        (x[12] or x[1] or x[24]) and (x[12] or not x[1] or not x[24]) and (not x[12] or x[1] or not x[24]) and (not x[12] or not x[1] or x[24]),
        (x[13] or x[2] or x[25]) and (x[13] or not x[2] or not x[25]) and (not x[13] or x[2] or not x[25]) and (not x[13] or not x[2] or x[25]),
        (x[14] or x[3] or x[26]) and (x[14] or not x[3] or not x[26]) and (not x[14] or x[3] or not x[26]) and (not x[14] or not x[3] or x[26]),
        (x[15] or x[4] or x[27]) and (x[15] or not x[4] or not x[27]) and (not x[15] or x[4] or not x[27]) and (not x[15] or not x[4] or x[27]),
        (x[16] or x[5] or x[28]) and (x[16] or not x[5] or not x[28]) and (not x[16] or x[5] or not x[28]) and (not x[16] or not x[5] or x[28]),
        (x[17] or x[6] or x[29]) and (x[17] or not x[6] or not x[29]) and (not x[17] or x[6] or not x[29]) and (not x[17] or not x[6] or x[29]),
        (x[18] or x[7] or x[30]) and (x[18] or not x[7] or not x[30]) and (not x[18] or x[7] or not x[30]) and (not x[18] or not x[7] or x[30]),
        (x[19] or x[8] or x[31]) and (x[19] or not x[8] or not x[31]) and (not x[19] or x[8] or not x[31]) and (not x[19] or not x[8] or x[31]),
        (x[20] or x[9] or x[0]) and (x[20] or not x[9] or not x[0]) and (not x[20] or x[9] or not x[0]) and (not x[20] or not x[9] or x[0]),
        (x[21] or x[10] or x[1]) and (x[21] or not x[10] or not x[1]) and (not x[21] or x[10] or not x[1]) and (not x[21] or not x[10] or x[1]),
        (x[22] or x[11] or x[2]) and (x[22] or not x[11] or not x[2]) and (not x[22] or x[11] or not x[2]) and (not x[22] or not x[11] or x[2]),
        (x[23] or x[12] or x[3]) and (x[23] or not x[12] or not x[3]) and (not x[23] or x[12] or not x[3]) and (not x[23] or not x[12] or x[3]),
        (x[24] or x[13] or x[4]) and (x[24] or not x[13] or not x[4]) and (not x[24] or x[13] or not x[4]) and (not x[24] or not x[13] or x[4]),
        (x[25] or x[14] or x[5]) and (x[25] or not x[14] or not x[5]) and (not x[25] or x[14] or not x[5]) and (not x[25] or not x[14] or x[5]),
        (x[26] or x[15] or x[6]) and (x[26] or not x[15] or not x[6]) and (not x[26] or x[15] or not x[6]) and (not x[26] or not x[15] or x[6]),
        (x[27] or x[16] or x[7]) and (x[27] or not x[16] or not x[7]) and (not x[27] or x[16] or not x[7]) and (not x[27] or not x[16] or x[7]),
        (x[28] or x[17] or x[8]) and (x[28] or not x[17] or not x[8]) and (not x[28] or x[17] or not x[8]) and (not x[28] or not x[17] or x[8]),
        (x[29] or x[18] or x[9]) and (x[29] or not x[18] or not x[9]) and (not x[29] or x[18] or not x[9]) and (not x[29] or not x[18] or x[9])
    ]

def bool_e_1(x):
    return [
        (x[154] or x[149] or x[135]) and (x[154] or not x[149] or not x[135]) and (not x[154] or x[149] or not x[135]) and (not x[154] or not x[149] or x[135]),
        (x[155] or x[150] or x[136]) and (x[155] or not x[150] or not x[136]) and (not x[155] or x[150] or not x[136]) and (not x[155] or not x[150] or x[136]),
        (x[156] or x[151] or x[137]) and (x[156] or not x[151] or not x[137]) and (not x[156] or x[151] or not x[137]) and (not x[156] or not x[151] or x[137]),
        (x[157] or x[152] or x[138]) and (x[157] or not x[152] or not x[138]) and (not x[157] or x[152] or not x[138]) and (not x[157] or not x[152] or x[138]),
        (x[158] or x[153] or x[139]) and (x[158] or not x[153] or not x[139]) and (not x[158] or x[153] or not x[139]) and (not x[158] or not x[153] or x[139]),
        (x[159] or x[154] or x[140]) and (x[159] or not x[154] or not x[140]) and (not x[159] or x[154] or not x[140]) and (not x[159] or not x[154] or x[140]),
        (x[128] or x[155] or x[141]) and (x[128] or not x[155] or not x[141]) and (not x[128] or x[155] or not x[141]) and (not x[128] or not x[155] or x[141]),
        (x[129] or x[156] or x[142]) and (x[129] or not x[156] or not x[142]) and (not x[129] or x[156] or not x[142]) and (not x[129] or not x[156] or x[142]),
        (x[130] or x[157] or x[143]) and (x[130] or not x[157] or not x[143]) and (not x[130] or x[157] or not x[143]) and (not x[130] or not x[157] or x[143]),
        (x[131] or x[158] or x[144]) and (x[131] or not x[158] or not x[144]) and (not x[131] or x[158] or not x[144]) and (not x[131] or not x[158] or x[144]),
        (x[132] or x[159] or x[145]) and (x[132] or not x[159] or not x[145]) and (not x[132] or x[159] or not x[145]) and (not x[132] or not x[159] or x[145]),
        (x[133] or x[128] or x[146]) and (x[133] or not x[128] or not x[146]) and (not x[133] or x[128] or not x[146]) and (not x[133] or not x[128] or x[146]),
        (x[134] or x[129] or x[147]) and (x[134] or not x[129] or not x[147]) and (not x[134] or x[129] or not x[147]) and (not x[134] or not x[129] or x[147]),
        (x[135] or x[130] or x[148]) and (x[135] or not x[130] or not x[148]) and (not x[135] or x[130] or not x[148]) and (not x[135] or not x[130] or x[148]),
        (x[136] or x[131] or x[149]) and (x[136] or not x[131] or not x[149]) and (not x[136] or x[131] or not x[149]) and (not x[136] or not x[131] or x[149]),
        (x[137] or x[132] or x[150]) and (x[137] or not x[132] or not x[150]) and (not x[137] or x[132] or not x[150]) and (not x[137] or not x[132] or x[150]),
        (x[138] or x[133] or x[151]) and (x[138] or not x[133] or not x[151]) and (not x[138] or x[133] or not x[151]) and (not x[138] or not x[133] or x[151]),
        (x[139] or x[134] or x[152]) and (x[139] or not x[134] or not x[152]) and (not x[139] or x[134] or not x[152]) and (not x[139] or not x[134] or x[152]),
        (x[140] or x[135] or x[153]) and (x[140] or not x[135] or not x[153]) and (not x[140] or x[135] or not x[153]) and (not x[140] or not x[135] or x[153]),
        (x[141] or x[136] or x[154]) and (x[141] or not x[136] or not x[154]) and (not x[141] or x[136] or not x[154]) and (not x[141] or not x[136] or x[154]),
        (x[142] or x[137] or x[155]) and (x[142] or not x[137] or not x[155]) and (not x[142] or x[137] or not x[155]) and (not x[142] or not x[137] or x[155]),
        (x[143] or x[138] or x[156]) and (x[143] or not x[138] or not x[156]) and (not x[143] or x[138] or not x[156]) and (not x[143] or not x[138] or x[156]),
        (x[144] or x[139] or x[157]) and (x[144] or not x[139] or not x[157]) and (not x[144] or x[139] or not x[157]) and (not x[144] or not x[139] or x[157]),
        (x[145] or x[140] or x[158]) and (x[145] or not x[140] or not x[158]) and (not x[145] or x[140] or not x[158]) and (not x[145] or not x[140] or x[158]),
        (x[146] or x[141] or x[159]) and (x[146] or not x[141] or not x[159]) and (not x[146] or x[141] or not x[159]) and (not x[146] or not x[141] or x[159]),
        (x[147] or x[142] or x[128]) and (x[147] or not x[142] or not x[128]) and (not x[147] or x[142] or not x[128]) and (not x[147] or not x[142] or x[128]),
        (x[148] or x[143] or x[129]) and (x[148] or not x[143] or not x[129]) and (not x[148] or x[143] or not x[129]) and (not x[148] or not x[143] or x[129]),
        (x[149] or x[144] or x[130]) and (x[149] or not x[144] or not x[130]) and (not x[149] or x[144] or not x[130]) and (not x[149] or not x[144] or x[130]),
        (x[150] or x[145] or x[131]) and (x[150] or not x[145] or not x[131]) and (not x[150] or x[145] or not x[131]) and (not x[150] or not x[145] or x[131]),
        (x[151] or x[146] or x[132]) and (x[151] or not x[146] or not x[132]) and (not x[151] or x[146] or not x[132]) and (not x[151] or not x[146] or x[132]),
        (x[152] or x[147] or x[133]) and (x[152] or not x[147] or not x[133]) and (not x[152] or x[147] or not x[133]) and (not x[152] or not x[147] or x[133]),
        (x[153] or x[148] or x[134]) and (x[153] or not x[148] or not x[134]) and (not x[153] or x[148] or not x[134]) and (not x[153] or not x[148] or x[134])
    ]

def bool_Ch(x):
    return [
        (x[128] or x[192]) and (not x[128] or x[160]) and (x[160] or x[192]),
        (x[129] or x[193]) and (not x[129] or x[161]) and (x[161] or x[193]),
        (x[130] or x[194]) and (not x[130] or x[162]) and (x[162] or x[194]),
        (x[131] or x[195]) and (not x[131] or x[163]) and (x[163] or x[195]),
        (x[132] or x[196]) and (not x[132] or x[164]) and (x[164] or x[196]),
        (x[133] or x[197]) and (not x[133] or x[165]) and (x[165] or x[197]),
        (x[134] or x[198]) and (not x[134] or x[166]) and (x[166] or x[198]),
        (x[135] or x[199]) and (not x[135] or x[167]) and (x[167] or x[199]),
        (x[136] or x[200]) and (not x[136] or x[168]) and (x[168] or x[200]),
        (x[137] or x[201]) and (not x[137] or x[169]) and (x[169] or x[201]),
        (x[138] or x[202]) and (not x[138] or x[170]) and (x[170] or x[202]),
        (x[139] or x[203]) and (not x[139] or x[171]) and (x[171] or x[203]),
        (x[140] or x[204]) and (not x[140] or x[172]) and (x[172] or x[204]),
        (x[141] or x[205]) and (not x[141] or x[173]) and (x[173] or x[205]),
        (x[142] or x[206]) and (not x[142] or x[174]) and (x[174] or x[206]),
        (x[143] or x[207]) and (not x[143] or x[175]) and (x[175] or x[207]),
        (x[144] or x[208]) and (not x[144] or x[176]) and (x[176] or x[208]),
        (x[145] or x[209]) and (not x[145] or x[177]) and (x[177] or x[209]),
        (x[146] or x[210]) and (not x[146] or x[178]) and (x[178] or x[210]),
        (x[147] or x[211]) and (not x[147] or x[179]) and (x[179] or x[211]),
        (x[148] or x[212]) and (not x[148] or x[180]) and (x[180] or x[212]),
        (x[149] or x[213]) and (not x[149] or x[181]) and (x[181] or x[213]),
        (x[150] or x[214]) and (not x[150] or x[182]) and (x[182] or x[214]),
        (x[151] or x[215]) and (not x[151] or x[183]) and (x[183] or x[215]),
        (x[152] or x[216]) and (not x[152] or x[184]) and (x[184] or x[216]),
        (x[153] or x[217]) and (not x[153] or x[185]) and (x[185] or x[217]),
        (x[154] or x[218]) and (not x[154] or x[186]) and (x[186] or x[218]),
        (x[155] or x[219]) and (not x[155] or x[187]) and (x[187] or x[219]),
        (x[156] or x[220]) and (not x[156] or x[188]) and (x[188] or x[220]),
        (x[157] or x[221]) and (not x[157] or x[189]) and (x[189] or x[221]),
        (x[158] or x[222]) and (not x[158] or x[190]) and (x[190] or x[222]),
        (x[159] or x[223]) and (not x[159] or x[191]) and (x[191] or x[223])
    ]

def bool_Maj(x):
    return [
        (x[0] or x[32]) and (x[0] or x[64]) and (x[32] or x[64]),
        (x[1] or x[33]) and (x[1] or x[65]) and (x[33] or x[65]),
        (x[2] or x[34]) and (x[2] or x[66]) and (x[34] or x[66]),
        (x[3] or x[35]) and (x[3] or x[67]) and (x[35] or x[67]),
        (x[4] or x[36]) and (x[4] or x[68]) and (x[36] or x[68]),
        (x[5] or x[37]) and (x[5] or x[69]) and (x[37] or x[69]),
        (x[6] or x[38]) and (x[6] or x[70]) and (x[38] or x[70]),
        (x[7] or x[39]) and (x[7] or x[71]) and (x[39] or x[71]),
        (x[8] or x[40]) and (x[8] or x[72]) and (x[40] or x[72]),
        (x[9] or x[41]) and (x[9] or x[73]) and (x[41] or x[73]),
        (x[10] or x[42]) and (x[10] or x[74]) and (x[42] or x[74]),
        (x[11] or x[43]) and (x[11] or x[75]) and (x[43] or x[75]),
        (x[12] or x[44]) and (x[12] or x[76]) and (x[44] or x[76]),
        (x[13] or x[45]) and (x[13] or x[77]) and (x[45] or x[77]),
        (x[14] or x[46]) and (x[14] or x[78]) and (x[46] or x[78]),
        (x[15] or x[47]) and (x[15] or x[79]) and (x[47] or x[79]),
        (x[16] or x[48]) and (x[16] or x[80]) and (x[48] or x[80]),
        (x[17] or x[49]) and (x[17] or x[81]) and (x[49] or x[81]),
        (x[18] or x[50]) and (x[18] or x[82]) and (x[50] or x[82]),
        (x[19] or x[51]) and (x[19] or x[83]) and (x[51] or x[83]),
        (x[20] or x[52]) and (x[20] or x[84]) and (x[52] or x[84]),
        (x[21] or x[53]) and (x[21] or x[85]) and (x[53] or x[85]),
        (x[22] or x[54]) and (x[22] or x[86]) and (x[54] or x[86]),
        (x[23] or x[55]) and (x[23] or x[87]) and (x[55] or x[87]),
        (x[24] or x[56]) and (x[24] or x[88]) and (x[56] or x[88]),
        (x[25] or x[57]) and (x[25] or x[89]) and (x[57] or x[89]),
        (x[26] or x[58]) and (x[26] or x[90]) and (x[58] or x[90]),
        (x[27] or x[59]) and (x[27] or x[91]) and (x[59] or x[91]),
        (x[28] or x[60]) and (x[28] or x[92]) and (x[60] or x[92]),
        (x[29] or x[61]) and (x[29] or x[93]) and (x[61] or x[93]),
        (x[30] or x[62]) and (x[30] or x[94]) and (x[62] or x[94]),
        (x[31] or x[63]) and (x[31] or x[95]) and (x[63] or x[95])
    ]

def bool_s_0(x):
    return [
        (x[14] or x[25]) and (not x[14] or not x[25]),
        (x[15] or x[26]) and (not x[15] or not x[26]),
        (x[16] or x[27]) and (not x[16] or not x[27]),
        (x[28] or x[17] or x[0]) and (x[28] or not x[17] or not x[0]) and (not x[28] or x[17] or not x[0]) and (not x[28] or not x[17] or x[0]),
        (x[29] or x[18] or x[1]) and (x[29] or not x[18] or not x[1]) and (not x[29] or x[18] or not x[1]) and (not x[29] or not x[18] or x[1]),
        (x[30] or x[19] or x[2]) and (x[30] or not x[19] or not x[2]) and (not x[30] or x[19] or not x[2]) and (not x[30] or not x[19] or x[2]),
        (x[31] or x[20] or x[3]) and (x[31] or not x[20] or not x[3]) and (not x[31] or x[20] or not x[3]) and (not x[31] or not x[20] or x[3]),
        (x[0] or x[21] or x[4]) and (x[0] or not x[21] or not x[4]) and (not x[0] or x[21] or not x[4]) and (not x[0] or not x[21] or x[4]),
        (x[1] or x[22] or x[5]) and (x[1] or not x[22] or not x[5]) and (not x[1] or x[22] or not x[5]) and (not x[1] or not x[22] or x[5]),
        (x[2] or x[23] or x[6]) and (x[2] or not x[23] or not x[6]) and (not x[2] or x[23] or not x[6]) and (not x[2] or not x[23] or x[6]),
        (x[3] or x[24] or x[7]) and (x[3] or not x[24] or not x[7]) and (not x[3] or x[24] or not x[7]) and (not x[3] or not x[24] or x[7]),
        (x[4] or x[25] or x[8]) and (x[4] or not x[25] or not x[8]) and (not x[4] or x[25] or not x[8]) and (not x[4] or not x[25] or x[8]),
        (x[5] or x[26] or x[9]) and (x[5] or not x[26] or not x[9]) and (not x[5] or x[26] or not x[9]) and (not x[5] or not x[26] or x[9]),
        (x[6] or x[27] or x[10]) and (x[6] or not x[27] or not x[10]) and (not x[6] or x[27] or not x[10]) and (not x[6] or not x[27] or x[10]),
        (x[7] or x[28] or x[11]) and (x[7] or not x[28] or not x[11]) and (not x[7] or x[28] or not x[11]) and (not x[7] or not x[28] or x[11]),
        (x[8] or x[29] or x[12]) and (x[8] or not x[29] or not x[12]) and (not x[8] or x[29] or not x[12]) and (not x[8] or not x[29] or x[12]),
        (x[9] or x[30] or x[13]) and (x[9] or not x[30] or not x[13]) and (not x[9] or x[30] or not x[13]) and (not x[9] or not x[30] or x[13]),
        (x[10] or x[31] or x[14]) and (x[10] or not x[31] or not x[14]) and (not x[10] or x[31] or not x[14]) and (not x[10] or not x[31] or x[14]),
        (x[11] or x[0] or x[15]) and (x[11] or not x[0] or not x[15]) and (not x[11] or x[0] or not x[15]) and (not x[11] or not x[0] or x[15]),
        (x[12] or x[1] or x[16]) and (x[12] or not x[1] or not x[16]) and (not x[12] or x[1] or not x[16]) and (not x[12] or not x[1] or x[16]),
        (x[13] or x[2] or x[17]) and (x[13] or not x[2] or not x[17]) and (not x[13] or x[2] or not x[17]) and (not x[13] or not x[2] or x[17]),
        (x[14] or x[3] or x[18]) and (x[14] or not x[3] or not x[18]) and (not x[14] or x[3] or not x[18]) and (not x[14] or not x[3] or x[18]),
        (x[15] or x[4] or x[19]) and (x[15] or not x[4] or not x[19]) and (not x[15] or x[4] or not x[19]) and (not x[15] or not x[4] or x[19]),
        (x[16] or x[5] or x[20]) and (x[16] or not x[5] or not x[20]) and (not x[16] or x[5] or not x[20]) and (not x[16] or not x[5] or x[20]),
        (x[17] or x[6] or x[21]) and (x[17] or not x[6] or not x[21]) and (not x[17] or x[6] or not x[21]) and (not x[17] or not x[6] or x[21]),
        (x[18] or x[7] or x[22]) and (x[18] or not x[7] or not x[22]) and (not x[18] or x[7] or not x[22]) and (not x[18] or not x[7] or x[22]),
        (x[19] or x[8] or x[23]) and (x[19] or not x[8] or not x[23]) and (not x[19] or x[8] or not x[23]) and (not x[19] or not x[8] or x[23]),
        (x[20] or x[9] or x[24]) and (x[20] or not x[9] or not x[24]) and (not x[20] or x[9] or not x[24]) and (not x[20] or not x[9] or x[24]),
        (x[21] or x[10] or x[25]) and (x[21] or not x[10] or not x[25]) and (not x[21] or x[10] or not x[25]) and (not x[21] or not x[10] or x[25]),
        (x[22] or x[11] or x[26]) and (x[22] or not x[11] or not x[26]) and (not x[22] or x[11] or not x[26]) and (not x[22] or not x[11] or x[26]),
        (x[23] or x[12] or x[27]) and (x[23] or not x[12] or not x[27]) and (not x[23] or x[12] or not x[27]) and (not x[23] or not x[12] or x[27]),
        (x[24] or x[13] or x[28]) and (x[24] or not x[13] or not x[28]) and (not x[24] or x[13] or not x[28]) and (not x[24] or not x[13] or x[28])
    ]


def bool_s_1(x):
    return [
        (x[13] or x[15]) and (not x[13] or not x[15]),
        (x[14] or x[16]) and (not x[14] or not x[16]),
        (x[15] or x[17]) and (not x[15] or not x[17]),
        (x[16] or x[18]) and (not x[16] or not x[18]),
        (x[17] or x[19]) and (not x[17] or not x[19]),
        (x[18] or x[20]) and (not x[18] or not x[20]),
        (x[19] or x[21]) and (not x[19] or not x[21]),
        (x[20] or x[22]) and (not x[20] or not x[22]),
        (x[21] or x[23]) and (not x[21] or not x[23]),
        (x[22] or x[24]) and (not x[22] or not x[24]),
        (x[25] or x[23] or x[0]) and (x[25] or not x[23] or not x[0]) and (not x[25] or x[23] or not x[0]) and (not x[25] or not x[23] or x[0]),
        (x[26] or x[24] or x[1]) and (x[26] or not x[24] or not x[1]) and (not x[26] or x[24] or not x[1]) and (not x[26] or not x[24] or x[1]),
        (x[27] or x[25] or x[2]) and (x[27] or not x[25] or not x[2]) and (not x[27] or x[25] or not x[2]) and (not x[27] or not x[25] or x[2]),
        (x[28] or x[26] or x[3]) and (x[28] or not x[26] or not x[3]) and (not x[28] or x[26] or not x[3]) and (not x[28] or not x[26] or x[3]),
        (x[29] or x[27] or x[4]) and (x[29] or not x[27] or not x[4]) and (not x[29] or x[27] or not x[4]) and (not x[29] or not x[27] or x[4]),
        (x[30] or x[28] or x[5]) and (x[30] or not x[28] or not x[5]) and (not x[30] or x[28] or not x[5]) and (not x[30] or not x[28] or x[5]),
        (x[31] or x[29] or x[6]) and (x[31] or not x[29] or not x[6]) and (not x[31] or x[29] or not x[6]) and (not x[31] or not x[29] or x[6]),
        (x[0] or x[30] or x[7]) and (x[0] or not x[30] or not x[7]) and (not x[0] or x[30] or not x[7]) and (not x[0] or not x[30] or x[7]),
        (x[1] or x[31] or x[8]) and (x[1] or not x[31] or not x[8]) and (not x[1] or x[31] or not x[8]) and (not x[1] or not x[31] or x[8]),
        (x[2] or x[0] or x[9]) and (x[2] or not x[0] or not x[9]) and (not x[2] or x[0] or not x[9]) and (not x[2] or not x[0] or x[9]),
        (x[3] or x[1] or x[10]) and (x[3] or not x[1] or not x[10]) and (not x[3] or x[1] or not x[10]) and (not x[3] or not x[1] or x[10]),
        (x[4] or x[2] or x[11]) and (x[4] or not x[2] or not x[11]) and (not x[4] or x[2] or not x[11]) and (not x[4] or not x[2] or x[11]),
        (x[5] or x[3] or x[12]) and (x[5] or not x[3] or not x[12]) and (not x[5] or x[3] or not x[12]) and (not x[5] or not x[3] or x[12]),
        (x[6] or x[4] or x[13]) and (x[6] or not x[4] or not x[13]) and (not x[6] or x[4] or not x[13]) and (not x[6] or not x[4] or x[13]),
        (x[7] or x[5] or x[14]) and (x[7] or not x[5] or not x[14]) and (not x[7] or x[5] or not x[14]) and (not x[7] or not x[5] or x[14]),
        (x[8] or x[6] or x[15]) and (x[8] or not x[6] or not x[15]) and (not x[8] or x[6] or not x[15]) and (not x[8] or not x[6] or x[15]),
        (x[9] or x[7] or x[16]) and (x[9] or not x[7] or not x[16]) and (not x[9] or x[7] or not x[16]) and (not x[9] or not x[7] or x[16]),
        (x[10] or x[8] or x[17]) and (x[10] or not x[8] or not x[17]) and (not x[10] or x[8] or not x[17]) and (not x[10] or not x[8] or x[17]),
        (x[11] or x[9] or x[18]) and (x[11] or not x[9] or not x[18]) and (not x[11] or x[9] or not x[18]) and (not x[11] or not x[9] or x[18]),
        (x[12] or x[10] or x[19]) and (x[12] or not x[10] or not x[19]) and (not x[12] or x[10] or not x[19]) and (not x[12] or not x[10] or x[19]),
        (x[13] or x[11] or x[20]) and (x[13] or not x[11] or not x[20]) and (not x[13] or x[11] or not x[20]) and (not x[13] or not x[11] or x[20]),
        (x[14] or x[12] or x[21]) and (x[14] or not x[12] or not x[21]) and (not x[14] or x[12] or not x[21]) and (not x[14] or not x[12] or x[21])
    ]

def message_pre_pro(string_input):
    bit_list = []
    for i in range(len(string_input)):
        bit_list.extend([True if b == '1' else False for b in format(ord(string_input[i]),'08b')])
    pad_one = bit_list + [True]
    back_append_0 = [False] * ((448 - len(pad_one)) % 512)
    back_append_1 = [True if b == '1' else False for b in format(len(bit_list),'064b')]
    full_bit_list = pad_one + back_append_0 + back_append_1
    return [full_bit_list[x:x+32] for x in range(0, len(full_bit_list), 32)]

def iteration(bool_values, w_t, k_t):
    t_1 = bool_32_addition(w_t, k_t) # w_t + k_t
    t_1 = bool_32_addition(t_1, bool_values[224:256]) # h + w_t + k_t
    t_1 = bool_32_addition(t_1, bool_e_1(bool_values)) # e1(e) + h + w_t + k_t
    t_1 = bool_32_addition(t_1, bool_Ch(bool_values))
    t_2 = bool_32_addition(bool_e_0(bool_values), bool_Maj(bool_values))
    return bool_32_addition(t_1, t_2) + bool_values[0:32] + bool_values[32:64] + bool_values[64:96] + bool_32_addition(bool_values[96:128], t_1) + bool_values[128:160] + bool_values[160:192] + bool_values[192:224]

def update(h_t, w_t):
    bool_values = h_t
    for i in range(64):
        if i > 15:
            r1 = bool_32_addition(bool_s_1(w_t[i-2]), w_t[i-7])
            r2 = bool_32_addition(bool_s_0(w_t[i-15]),  w_t[i-16])
            w_t.append(bool_32_addition(r1, r2))
        bool_values = iteration(bool_values, w_t[i], sha_bool_constants[i])
    for x in range(0, 256, 32):
        bool_values[x:x+32] = bool_32_addition(bool_values[x:x+32], h_t[x:x+32])
    return bool_values

def sha256(input_string):
    h_t = initial_bool_values
    preprocessed_input = message_pre_pro(input_string)
    for i in range(0, len(preprocessed_input), 16):
        h_t = update(h_t, preprocessed_input[i:i+16])
    return h_t

msg = "0xDEADBEEF"
custom_implem = format(int(''.join(['1' if b else '0' for b in sha256(msg)]),2),'064x')
classic_implem = hashlib.sha256(msg).hexdigest()

print ''.join(['1' if b else '0' for b in sha256(msg)])
print custom_implem
print  classic_implem

assert custom_implem == classic_implem
