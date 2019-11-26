#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "../include/karloff_zwick.h"
#include "../include/hash.h"

#define INPUT_SIZE 8

int main (int argc, char* argv[]) {
  int i, j;
  cnf * cnf;
  value** hashed;
  kz_value res;
  char input = 0xffffff9b;
  value** target_hash;
  do {
    target_hash = hash(NULL, &input, 0);
    fprintf(stdout, "===== SHA256(0x%x) =====\n", input);
    cnf = new_cnf();
    hashed = hash(cnf, "", INPUT_SIZE);
    for (i = 0; i < 256; i++) {
      if (hashed[i]->type == variable) {
        if (target_hash[i]->value.b == true) {
          fix_value(cnf, hashed[i]->value.l);
        } else {
          fix_value(cnf, -hashed[i]->value.l);
        }
      } else {
        fprintf(stderr, "hashed[%i] is a constant.\n", i);
        EXIT_FAILURE;
      }
    }

    res = karloff_zwick(cnf);
    fprintf(stdout, "=> %llu / %llu\n", res.nb_sat, res.nb_sat+res.nb_unsat);

    free_word(target_hash, 256);
    free_word(hashed, 256);
    del_cnf(cnf);
    input++;
  } while (input != 0);
  return EXIT_SUCCESS;
}
