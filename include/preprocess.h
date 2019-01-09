#ifndef PREPROCESS_H
#define PREPROCESS_H

#include "./graph.h"

#define BLOCK_SIZE 512

int nbBlocksNeeded(int);

node** preProcessInput(char*);

#endif
