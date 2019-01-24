#include <stdlib.h>
#include <string.h>
#include "../include/preprocess.h"

/*
 * Process the number of blocks needed with the input len in bits.
 */
int nbBlocksNeeded(int input_len, int nonce_size) {
  int nb_blocks = (input_len + nonce_size) / 512;
  if ((input_len + nonce_size) % 512 > 440) {
    nb_blocks = nb_blocks + 2;
  } else {
    nb_blocks = nb_blocks + 1;
  }
  return nb_blocks;
}

/*
 * Process a bytes input and return a list of values.
 */
value** preProcessInput(cnf* c, char* input, int nonce_size) {
  value** result;
  __int64_t input_len = strlen(input) << 3;
  int cpt = 0, nb_blocks = nbBlocksNeeded(input_len, nonce_size);
  result = malloc(sizeof(value*) * nb_blocks * BLOCK_SIZE);

  /* Read input */
  for (; cpt < input_len >> 3; cpt++) {
    result[cpt<<3]     = new_boolean((input[cpt] >> 7) & 1);
    result[(cpt<<3)+1] = new_boolean((input[cpt] >> 6) & 1);
    result[(cpt<<3)+2] = new_boolean((input[cpt] >> 5) & 1);
    result[(cpt<<3)+3] = new_boolean((input[cpt] >> 4) & 1);
    result[(cpt<<3)+4] = new_boolean((input[cpt] >> 3) & 1);
    result[(cpt<<3)+5] = new_boolean((input[cpt] >> 2) & 1);
    result[(cpt<<3)+6] = new_boolean((input[cpt] >> 1) & 1);
    result[(cpt<<3)+7] = new_boolean(input[cpt] & 1);
  }
  cpt = 8*cpt;

  /* Add nonce */
  input_len = input_len + nonce_size;
  for (; cpt < input_len; cpt++) {
    result[cpt] = new_litteral(c);
  }
  /* Bit padding */
  result[cpt] =  new_boolean(true);
  for (cpt = cpt+1; cpt < (nb_blocks * BLOCK_SIZE) - 64; cpt++) {
    result[cpt] = new_boolean(false);
  }
  for (cpt = (nb_blocks * BLOCK_SIZE) - 1; cpt > (nb_blocks * BLOCK_SIZE) - 65; cpt--) {
    result[cpt] = new_boolean(input_len & 1);
    input_len = input_len >> 1;
  }
  return result;
}
