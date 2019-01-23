#include <stdlib.h>
#include <string.h>
#include "../include/preprocess.h"

/*
 * Process the number of blocks needed with the input len in bits.
 */
int nbBlocksNeeded(int input_len) {
  int nb_blocks = input_len / 512;
  if (input_len % 512 > 440) {
    nb_blocks = nb_blocks + 2;
  } else {
    nb_blocks = nb_blocks + 1;
  }
  return nb_blocks;
}

/*
 * Process a bytes input and return a list of values.
 */
value** preProcessInput(cnf* c, char* input) {
  value** result;
  __int64_t input_len = strlen(input);
  int cpt = 0, nb_blocks = nbBlocksNeeded(input_len << 3);
  result = malloc(sizeof(value*) * nb_blocks * BLOCK_SIZE);

  /* Read input */
  for (; cpt < input_len; cpt = cpt + 1) {
    result[8*cpt] =   new_boolean((input[cpt] >> 7) & 1);
    result[8*cpt+1] = new_boolean((input[cpt] >> 6) & 1);
    result[8*cpt+2] = new_boolean((input[cpt] >> 5) & 1);
    result[8*cpt+3] = new_boolean((input[cpt] >> 4) & 1);
    result[8*cpt+4] = new_boolean((input[cpt] >> 3) & 1);
    result[8*cpt+5] = new_boolean((input[cpt] >> 2) & 1);
    result[8*cpt+6] = new_boolean((input[cpt] >> 1) & 1);
    result[8*cpt+7] = new_boolean(input[cpt] & 1);
  }

  /* Bit padding */
  result[8*cpt] =  new_boolean(true);
  for (cpt = 8*cpt+1; cpt < (nb_blocks * BLOCK_SIZE) - 64; cpt++) {
    result[cpt] = new_boolean(false);
  }
  input_len = input_len << 3;
  for (cpt = (nb_blocks * BLOCK_SIZE) - 1; cpt > (nb_blocks * BLOCK_SIZE) - 65; cpt--) {
    result[cpt] = new_boolean(input_len & 1);
    input_len = input_len >> 1;
  }
  return result;
}
