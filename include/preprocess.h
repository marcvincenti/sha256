#ifndef PREPROCESS_H
#define PREPROCESS_H

#include "./cnf.h"
#include "./hash.h"

int nbBlocksNeeded(int, int);

value** preProcessInput(cnf*, char*, int);

#endif
