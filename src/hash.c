#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "../include/hash.h"
#include "../include/operations.h"
#include "../include/preprocess.h"

const char INIT_SHA_VALUES[256] = { \
  0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, \
  1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, \
  0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, \
  1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, \
  0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, \
  1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, \
  0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, \
  0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1  \
};

/*
 * Calculate w_t with a given 512-bit chunk
 */
char* process_wt(char* w_t, char* chunk) {
  int i;
  char* s0, * s1, * r0, * r1, * res;
  memcpy(w_t, chunk, 512);
  for (i = 16; i < 64; i++ ) {
    s0 = bool_s_0(&w_t[(i-15)*32]);
    r0 = bool_add_32(s0, &w_t[(i-16)*32]);
    s1 = bool_s_1(&w_t[(i-2)*32]);
    r1 = bool_add_32(s1, &w_t[(i-7)*32]);
    res = bool_add_32(r0, r1);
    memcpy(&w_t[i*32], res, 32);
    free(s0);
    free(s1);
    free(r0);
    free(r1);
    free(res);
  }
  return w_t;
}

char* update(char h_t[], char w_t[]) {
  return h_t;
}

/*
 * Process an input of bytes and return a list of bits
 */
char* hash(char* input) {
  char* w_t = malloc(2048);
  char* h_t = memcpy(malloc(256), &INIT_SHA_VALUES, 256);
  char* chunks = preProcessInput(input);
  int nb_blocks = nbBlocksNeeded(strlen(input));
  int i;
  for (i = 0; i < nb_blocks; i++) {
    /* prepare w_t */
    process_wt(w_t, chunks+512*i);
    /* update h_t with w_t */
    h_t = update(h_t, w_t);
  }
  free(w_t);
  free(chunks);
  return h_t;
}
