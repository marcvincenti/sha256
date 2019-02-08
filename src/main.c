#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "../include/karloff_zwick.h"
#include "../include/hash.h"

int main (int argc, char* argv[]) {
  int i, j, k;
  cnf* cnf;
  boolean has_failed;
  value** hashed;
  kz_value res;
  char* prefix = "0xDEADBEEF";
  for (i = 1; i < 5; i++) {
    fprintf(stdout, "===== { prefix: \"%s\", nonce: %i bytes } =====\n", prefix, i);
    has_failed = false;
    for (j = 8; j < 64 && has_failed == false; j+=8) {
      cnf = new_cnf();
      hashed = hash(cnf, prefix, i << 3);
      for (k = 0; k < j; k++) {
        if (hashed[k]->type == variable) {
          fix_value(cnf, -hashed[k]->value.l);
        } else {
          fprintf(stderr, "hashed[%i] is a constant.\n", k);
          EXIT_FAILURE;
        }
      }
      res = karloff_zwick(cnf);
      fprintf(stdout, " { neg_bits: %i, nb_sat: %llu, nb_unsat: %llu } ", j, res.nb_sat, res.nb_unsat);
      if (res.nb_unsat <= (res.nb_unsat+res.nb_sat) >> 3) {
        fprintf(stdout, " => OK");
      } else {
        fprintf(stdout, " => NOT OK");
        has_failed = true;
      }
      fprintf(stdout, " (%f)\n", (float)res.nb_unsat / (res.nb_unsat+res.nb_sat));
      del_cnf(cnf);
    }
    fprintf(stdout, "\n");
  }
  return EXIT_SUCCESS;
}
