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
        x[30] ^ x[19] ^ x[10],
        x[31] ^ x[20] ^ x[11],
        x[0] ^ x[21] ^ x[12],
        x[1] ^ x[22] ^ x[13],
        x[2] ^ x[23] ^ x[14],
        x[3] ^ x[24] ^ x[15],
        x[4] ^ x[25] ^ x[16],
        x[5] ^ x[26] ^ x[17],
        x[6] ^ x[27] ^ x[18],
        x[7] ^ x[28] ^ x[19],
        x[8] ^ x[29] ^ x[20],
        x[9] ^ x[30] ^ x[21],
        x[10] ^ x[31] ^ x[22],
        x[11] ^ x[0] ^ x[23],
        x[12] ^ x[1] ^ x[24],
        x[13] ^ x[2] ^ x[25],
        x[14] ^ x[3] ^ x[26],
        x[15] ^ x[4] ^ x[27],
        x[16] ^ x[5] ^ x[28],
        x[17] ^ x[6] ^ x[29],
        x[18] ^ x[7] ^ x[30],
        x[19] ^ x[8] ^ x[31],
        x[20] ^ x[9] ^ x[0],
        x[21] ^ x[10] ^ x[1],
        x[22] ^ x[11] ^ x[2],
        x[23] ^ x[12] ^ x[3],
        x[24] ^ x[13] ^ x[4],
        x[25] ^ x[14] ^ x[5],
        x[26] ^ x[15] ^ x[6],
        x[27] ^ x[16] ^ x[7],
        x[28] ^ x[17] ^ x[8],
        x[29] ^ x[18] ^ x[9]
    ]

def bool_e_1(x):
    return [
        x[26] ^ x[21] ^ x[7],
        x[27] ^ x[22] ^ x[8],
        x[28] ^ x[23] ^ x[9],
        x[29] ^ x[24] ^ x[10],
        x[30] ^ x[25] ^ x[11],
        x[31] ^ x[26] ^ x[12],
        x[0] ^ x[27] ^ x[13],
        x[1] ^ x[28] ^ x[14],
        x[2] ^ x[29] ^ x[15],
        x[3] ^ x[30] ^ x[16],
        x[4] ^ x[31] ^ x[17],
        x[5] ^ x[0] ^ x[18],
        x[6] ^ x[1] ^ x[19],
        x[7] ^ x[2] ^ x[20],
        x[8] ^ x[3] ^ x[21],
        x[9] ^ x[4] ^ x[22],
        x[10] ^ x[5] ^ x[23],
        x[11] ^ x[6] ^ x[24],
        x[12] ^ x[7] ^ x[25],
        x[13] ^ x[8] ^ x[26],
        x[14] ^ x[9] ^ x[27],
        x[15] ^ x[10] ^ x[28],
        x[16] ^ x[11] ^ x[29],
        x[17] ^ x[12] ^ x[30],
        x[18] ^ x[13] ^ x[31],
        x[19] ^ x[14] ^ x[0],
        x[20] ^ x[15] ^ x[1],
        x[21] ^ x[16] ^ x[2],
        x[22] ^ x[17] ^ x[3],
        x[23] ^ x[18] ^ x[4],
        x[24] ^ x[19] ^ x[5],
        x[25] ^ x[20] ^ x[6]
    ]

def bool_Ch(x, y, z):
    return [
        (x[0] and y[0]) or (not x[0] and z[0]),
        (x[1] and y[1]) or (not x[1] and z[1]),
        (x[2] and y[2]) or (not x[2] and z[2]),
        (x[3] and y[3]) or (not x[3] and z[3]),
        (x[4] and y[4]) or (not x[4] and z[4]),
        (x[5] and y[5]) or (not x[5] and z[5]),
        (x[6] and y[6]) or (not x[6] and z[6]),
        (x[7] and y[7]) or (not x[7] and z[7]),
        (x[8] and y[8]) or (not x[8] and z[8]),
        (x[9] and y[9]) or (not x[9] and z[9]),
        (x[10] and y[10]) or (not x[10] and z[10]),
        (x[11] and y[11]) or (not x[11] and z[11]),
        (x[12] and y[12]) or (not x[12] and z[12]),
        (x[13] and y[13]) or (not x[13] and z[13]),
        (x[14] and y[14]) or (not x[14] and z[14]),
        (x[15] and y[15]) or (not x[15] and z[15]),
        (x[16] and y[16]) or (not x[16] and z[16]),
        (x[17] and y[17]) or (not x[17] and z[17]),
        (x[18] and y[18]) or (not x[18] and z[18]),
        (x[19] and y[19]) or (not x[19] and z[19]),
        (x[20] and y[20]) or (not x[20] and z[20]),
        (x[21] and y[21]) or (not x[21] and z[21]),
        (x[22] and y[22]) or (not x[22] and z[22]),
        (x[23] and y[23]) or (not x[23] and z[23]),
        (x[24] and y[24]) or (not x[24] and z[24]),
        (x[25] and y[25]) or (not x[25] and z[25]),
        (x[26] and y[26]) or (not x[26] and z[26]),
        (x[27] and y[27]) or (not x[27] and z[27]),
        (x[28] and y[28]) or (not x[28] and z[28]),
        (x[29] and y[29]) or (not x[29] and z[29]),
        (x[30] and y[30]) or (not x[30] and z[30]),
        (x[31] and y[31]) or (not x[31] and z[31])
    ]

def bool_Maj(x, y, z):
    return [
        (x[0] and y[0]) or (x[0] and z[0]) or (y[0] and z[0]),
        (x[1] and y[1]) or (x[1] and z[1]) or (y[1] and z[1]),
        (x[2] and y[2]) or (x[2] and z[2]) or (y[2] and z[2]),
        (x[3] and y[3]) or (x[3] and z[3]) or (y[3] and z[3]),
        (x[4] and y[4]) or (x[4] and z[4]) or (y[4] and z[4]),
        (x[5] and y[5]) or (x[5] and z[5]) or (y[5] and z[5]),
        (x[6] and y[6]) or (x[6] and z[6]) or (y[6] and z[6]),
        (x[7] and y[7]) or (x[7] and z[7]) or (y[7] and z[7]),
        (x[8] and y[8]) or (x[8] and z[8]) or (y[8] and z[8]),
        (x[9] and y[9]) or (x[9] and z[9]) or (y[9] and z[9]),
        (x[10] and y[10]) or (x[10] and z[10]) or (y[10] and z[10]),
        (x[11] and y[11]) or (x[11] and z[11]) or (y[11] and z[11]),
        (x[12] and y[12]) or (x[12] and z[12]) or (y[12] and z[12]),
        (x[13] and y[13]) or (x[13] and z[13]) or (y[13] and z[13]),
        (x[14] and y[14]) or (x[14] and z[14]) or (y[14] and z[14]),
        (x[15] and y[15]) or (x[15] and z[15]) or (y[15] and z[15]),
        (x[16] and y[16]) or (x[16] and z[16]) or (y[16] and z[16]),
        (x[17] and y[17]) or (x[17] and z[17]) or (y[17] and z[17]),
        (x[18] and y[18]) or (x[18] and z[18]) or (y[18] and z[18]),
        (x[19] and y[19]) or (x[19] and z[19]) or (y[19] and z[19]),
        (x[20] and y[20]) or (x[20] and z[20]) or (y[20] and z[20]),
        (x[21] and y[21]) or (x[21] and z[21]) or (y[21] and z[21]),
        (x[22] and y[22]) or (x[22] and z[22]) or (y[22] and z[22]),
        (x[23] and y[23]) or (x[23] and z[23]) or (y[23] and z[23]),
        (x[24] and y[24]) or (x[24] and z[24]) or (y[24] and z[24]),
        (x[25] and y[25]) or (x[25] and z[25]) or (y[25] and z[25]),
        (x[26] and y[26]) or (x[26] and z[26]) or (y[26] and z[26]),
        (x[27] and y[27]) or (x[27] and z[27]) or (y[27] and z[27]),
        (x[28] and y[28]) or (x[28] and z[28]) or (y[28] and z[28]),
        (x[29] and y[29]) or (x[29] and z[29]) or (y[29] and z[29]),
        (x[30] and y[30]) or (x[30] and z[30]) or (y[30] and z[30]),
        (x[31] and y[31]) or (x[31] and z[31]) or (y[31] and z[31])
    ]

def bool_s_0(x):
    return [
        x[14] ^ x[25],
        x[15] ^ x[26],
        x[16] ^ x[27],
        x[28] ^ x[17] ^ x[0],
        x[29] ^ x[18] ^ x[1],
        x[30] ^ x[19] ^ x[2],
        x[31] ^ x[20] ^ x[3],
        x[0] ^ x[21] ^ x[4],
        x[1] ^ x[22] ^ x[5],
        x[2] ^ x[23] ^ x[6],
        x[3] ^ x[24] ^ x[7],
        x[4] ^ x[25] ^ x[8],
        x[5] ^ x[26] ^ x[9],
        x[6] ^ x[27] ^ x[10],
        x[7] ^ x[28] ^ x[11],
        x[8] ^ x[29] ^ x[12],
        x[9] ^ x[30] ^ x[13],
        x[10] ^ x[31] ^ x[14],
        x[11] ^ x[0] ^ x[15],
        x[12] ^ x[1] ^ x[16],
        x[13] ^ x[2] ^ x[17],
        x[14] ^ x[3] ^ x[18],
        x[15] ^ x[4] ^ x[19],
        x[16] ^ x[5] ^ x[20],
        x[17] ^ x[6] ^ x[21],
        x[18] ^ x[7] ^ x[22],
        x[19] ^ x[8] ^ x[23],
        x[20] ^ x[9] ^ x[24],
        x[21] ^ x[10] ^ x[25],
        x[22] ^ x[11] ^ x[26],
        x[23] ^ x[12] ^ x[27],
        x[24] ^ x[13] ^ x[28]
    ]


def bool_s_1(x):
    return [
        x[13] ^ x[15],
        x[14] ^ x[16],
        x[15] ^ x[17],
        x[16] ^ x[18],
        x[17] ^ x[19],
        x[18] ^ x[20],
        x[19] ^ x[21],
        x[20] ^ x[22],
        x[21] ^ x[23],
        x[22] ^ x[24],
        x[25] ^ x[23] ^ x[0],
        x[26] ^ x[24] ^ x[1],
        x[27] ^ x[25] ^ x[2],
        x[28] ^ x[26] ^ x[3],
        x[29] ^ x[27] ^ x[4],
        x[30] ^ x[28] ^ x[5],
        x[31] ^ x[29] ^ x[6],
        x[0] ^ x[30] ^ x[7],
        x[1] ^ x[31] ^ x[8],
        x[2] ^ x[0] ^ x[9],
        x[3] ^ x[1] ^ x[10],
        x[4] ^ x[2] ^ x[11],
        x[5] ^ x[3] ^ x[12],
        x[6] ^ x[4] ^ x[13],
        x[7] ^ x[5] ^ x[14],
        x[8] ^ x[6] ^ x[15],
        x[9] ^ x[7] ^ x[16],
        x[10] ^ x[8] ^ x[17],
        x[11] ^ x[9] ^ x[18],
        x[12] ^ x[10] ^ x[19],
        x[13] ^ x[11] ^ x[20],
        x[14] ^ x[12] ^ x[21]
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
    t_1 = bool_32_addition(t_1, bool_e_1(bool_values[128:160])) # e1(e) + h + w_t + k_t
    t_1 = bool_32_addition(t_1, bool_Ch(bool_values[128:160], bool_values[160:192], bool_values[192:224]))
    t_2 = bool_32_addition(bool_e_0(bool_values[0:32]), bool_Maj(bool_values[0:32], bool_values[32:64], bool_values[64:96]))
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
#custom_implem = format(int(''.join(['1' if b else '0' for b in sha256(msg)]),2),'064x')
#classic_implem = hashlib.sha256(msg).hexdigest()

print ''.join(['1' if b else '0' for b in sha256(msg)])
#print custom_implem
#print  classic_implem

#assert custom_implem == classic_implem
