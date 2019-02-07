#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "../include/karloff_zwick.h"
#include "../include/hash.h"

int main (int argc, char* argv[]) {
  int i;
  cnf* cnf;
  kz_value res;
  if (argc == 2) {
    cnf = new_cnf();
    hash(cnf, "", strlen(argv[1]) << 3);
    res = karloff_zwick(cnf);
    fprintf(stdout, "nb_sat: %llu\n", res.nb_sat);
    fprintf(stdout, "nb_unsat: %llu\n", res.nb_unsat);
    del_cnf(cnf);
    return EXIT_SUCCESS;
  } else {
    fprintf(stderr, "illegal usage of %s\n", argv[0]);
    fprintf(stderr, "usage: %s [message]\n", argv[0]);
    return EXIT_FAILURE;
  }
}
