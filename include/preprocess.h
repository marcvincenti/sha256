#ifndef PREPROCESS_H
#define PREPROCESS_H

#include "./cnf.h"

#define BLOCK_SIZE 512

int nbBlocksNeeded(int);

value** preProcessInput(cnf*, char*);

#endif
