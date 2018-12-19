#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "../include/preprocess.h"

/*
 * Process the number of blocks needed with the input len in bytes.
 */
int nbBlocksNeeded(int input_len) {
  int nb_blocks = input_len / 64;
  if (input_len % 64 > 55) {
    nb_blocks = nb_blocks + 2;
  } else {
    nb_blocks = nb_blocks + 1;
  }
  return nb_blocks;
}

/*
 * Process an input of bytes and return a list of bits.
 * The result need to be freed
 */
char* preProcessInput(char* input) {
  char* result;
  __int64_t input_len = strlen(input);
  int cpt = 0, nb_blocks = nbBlocksNeeded(input_len);
  result = malloc(nb_blocks * BLOCK_SIZE);

  /* Read input */
  for (; cpt < input_len; cpt = cpt + 1) {
    result[8*cpt] = input[cpt] & 128 ? 1 : 0;
    result[8*cpt+1] = input[cpt] & 64 ? 1 : 0;
    result[8*cpt+2] = input[cpt] & 32 ? 1 : 0;
    result[8*cpt+3] = input[cpt] & 16 ? 1 : 0;
    result[8*cpt+4] = input[cpt] & 8 ? 1 : 0;
    result[8*cpt+5] = input[cpt] & 4 ? 1 : 0;
    result[8*cpt+6] = input[cpt] & 2 ? 1 : 0;
    result[8*cpt+7] = input[cpt] & 1 ? 1 : 0;
  }

  /* Bit padding */
  result[8*cpt] = 1;
  for (cpt = 8*cpt+1; cpt < (nb_blocks * BLOCK_SIZE) - 64; cpt++) {
    result[cpt] = 0;
  }
  input_len = input_len << 3;
  for (cpt = (nb_blocks * BLOCK_SIZE) - 1; cpt > (nb_blocks * BLOCK_SIZE) - 65; cpt--) {
    result[cpt] = input_len & 1;
    input_len = input_len >> 1;
  }
  return result;
}
