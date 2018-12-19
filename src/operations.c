#include <stdlib.h>
#include "../include/operations.h"

/*
 * Process a 32bits addition
 * The result need to be freed
 */
char* bool_add_32(char a[], char b[]) {
  int i;
  char* res = malloc(32);
  char r[32];
  r[31] = a[31] && b[31];
  res[31] = a[31] ^ b[31];
  for (i = 30; i > -1; i--) {
    res[i] = a[i] ^ b[i] ^ r[i+1];
    r[i] = (a[i] && b[i]) || (a[i] && r[i+1]) || (b[i] && r[i+1]);
  }
  return res;
}

/*
 * Process a S0 word function
 * The result need to be freed
 */
char* bool_s_0(char* x) {
  int i = 0;
  char* res = malloc(32);
  for (; i < 3; i++) {
    res[i] = x[(i - 7) & 31] ^ x[(i - 18) & 31];
  }
  for (; i < 32; i++) {
    res[i] = x[(i - 7) & 31] ^ x[(i - 18) & 31] ^ x[i - 3];
  }
  return res;
}

/*
 * Process a S0 word function
 * The result need to be freed
 */
char* bool_s_1(char* x) {
  int i = 0;
  char* res = malloc(32);
  for (; i < 10; i++) {
    res[i] = x[(i - 17) & 31] ^ x[(i - 19) & 31];
  }
  for (; i < 32; i++) {
    res[i] = x[(i - 17) & 31] ^ x[(i - 19) & 31] ^ x[i - 10];
  }
  return res;
}
