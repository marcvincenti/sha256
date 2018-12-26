#include <stdio.h>
#include <stdlib.h>
#include "../include/hash.h"

int main (int argc, char* argv[]) {
  char* hashed;
  int j;
  if (argc == 2) {
    hashed = hash(argv[1]);
    for (j = 0; j < 256; j++) {
      if (hashed[j]) {
        fprintf(stdout, "1");
      } else {
        fprintf(stdout, "0");
      }
    }
    fprintf(stdout, "\n");
    free(hashed);
    return EXIT_SUCCESS;
  } else {
    fprintf(stderr, "illegal usage of %s\n", argv[0]);
    fprintf(stderr, "usage: %s [message]\n", argv[0]);
    return EXIT_FAILURE;
  }
}
