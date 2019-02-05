#!/usr/bin/env python

import hashlib

def process_min_digest(prefix, nb_bytes):
    min_digest = ''.join(['f']*64)
    min_word = 'ERROR'
    if nb_bytes > 1:
        for byte in range(0, 256):
            word, digest = process_min_digest(prefix + chr(byte), nb_bytes - 1)
            if digest < min_digest:
                min_digest = digest
                min_word = word
    else:
        for byte in range(0, 256):
            word = prefix + chr(byte)
            digest = hashlib.sha256(word).hexdigest()
            if digest < min_digest:
                min_digest = digest
                min_word = word
    return (min_word, min_digest)

prefix = "0xDEADBEEF"
print 'Using "' + prefix + '" as prefix'
for nb_bytes in range(1, 5):
    print 'With ' + str(nb_bytes) + ' byte(s):'
    min_word, min_digest = process_min_digest(prefix, nb_bytes)
    print str(map(int, bytearray(min_word))) + ' -> ' + min_digest
