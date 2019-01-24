#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "../include/cnf.h"
#include "../include/hash.h"

int main (int argc, char* argv[]) {
  value** hashed;
  int i;
  cnf* cnf;
  if (argc == 2) {
    cnf = new_cnf();
    hashed = hash(cnf, "", strlen(argv[1]) << 3);
    for (i = 0; i < 256; i++) {
      if (hashed[i]->type == constant) {
        if (hashed[i]->value.b) {
          fprintf(stdout, "1");
        } else {
          fprintf(stdout, "0");
        }
      }
    }
    fprintf(stdout, "\n");
    del_cnf(cnf);
    free(hashed);
    return EXIT_SUCCESS;
  } else {
    fprintf(stderr, "illegal usage of %s\n", argv[0]);
    fprintf(stderr, "usage: %s [message]\n", argv[0]);
    return EXIT_FAILURE;
  }
}
