#ifndef HASH_H
#define HASH_H

#include "./cnf.h"

#define BLOCK_SIZE 512
#define WORD_SIZE 32

value** hash(cnf*, char*, int);

#endif
