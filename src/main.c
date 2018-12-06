#include <stdio.h>
#include <stdlib.h>
#include "../include/preprocess.h"

int main (int argc, char* argv[]) {
  char* chunk;
  int i;
  if (argc == 2) {
    chunk = preProcessInput(argv[1]);
    return EXIT_SUCCESS;
  } else {
    fprintf(stderr, "illegal usage of %s\n", argv[0]);
    fprintf(stderr, "usage: %s [message]\n", argv[0]);
    return EXIT_FAILURE;
  }
}
