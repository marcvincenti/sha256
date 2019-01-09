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
 */
node** preProcessInput(char* input) {
  node** result;
  __int64_t input_len = strlen(input);
  int cpt = 0, nb_blocks = nbBlocksNeeded(input_len);
  result = malloc(sizeof(node*) * nb_blocks * BLOCK_SIZE);

  /* Read input */
  for (; cpt < input_len; cpt = cpt + 1) {
    result[8*cpt] =   new_constant((input[cpt] >> 7) & 1);
    result[8*cpt+1] = new_constant((input[cpt] >> 6) & 1);
    result[8*cpt+2] = new_constant((input[cpt] >> 5) & 1);
    result[8*cpt+3] = new_constant((input[cpt] >> 4) & 1);
    result[8*cpt+4] = new_constant((input[cpt] >> 3) & 1);
    result[8*cpt+5] = new_constant((input[cpt] >> 2) & 1);
    result[8*cpt+6] = new_constant((input[cpt] >> 1) & 1);
    result[8*cpt+7] = new_constant(input[cpt] & 1);
  }

  /* Bit padding */
  result[8*cpt] =  new_constant(1);
  for (cpt = 8*cpt+1; cpt < (nb_blocks * BLOCK_SIZE) - 64; cpt++) {
    result[cpt] = new_constant(0);
  }
  input_len = input_len << 3;
  for (cpt = (nb_blocks * BLOCK_SIZE) - 1; cpt > (nb_blocks * BLOCK_SIZE) - 65; cpt--) {
    result[cpt] = new_constant(input_len & 1);
    input_len = input_len >> 1;
  }
  return result;
}
