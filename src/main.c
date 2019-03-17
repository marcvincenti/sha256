#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "../include/karloff_zwick.h"
#include "../include/hash.h"

#define INPUT_SIZE 8

int main (int argc, char* argv[]) {
  int i, j;
  cnf * cnf, * temp_cnf;
  value** hashed;
  kz_value res;
  double approx;
  double worst_approx;
  int worst_assign;
  char input = 0xffffff9b;
  boolean assignements[INPUT_SIZE];
  value** target_hash;
  int valid_bytes = 0;
  int invalid_bytes = 0;
  do {
    target_hash = hash(NULL, &input, 0);
    for (i = 0; i < INPUT_SIZE; i++) { assignements[i] = false; }
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
    for (j = 0; j < INPUT_SIZE; j++) {
      worst_approx = 0;
      worst_assign = 0;
      for (i = -INPUT_SIZE; i <= INPUT_SIZE; i++) {
        if (i != 0 && assignements[abs(i)-1] == false) {
          temp_cnf = copy_cnf(cnf);
          fix_value(temp_cnf, i);
          res = karloff_zwick(temp_cnf);
          /* fprintf(stdout, " %i => { nb_sat: %llu, nb_unsat: %llu } \n", i, res.nb_sat, res.nb_unsat); */
          approx = (double)res.nb_unsat / (res.nb_unsat+res.nb_sat);
          if (worst_approx < approx) {
            worst_approx = approx;
            worst_assign = i;
          }
          del_cnf(temp_cnf);
        }
      }
      fprintf(stdout, "worst := %i", worst_assign);
      if ((worst_assign < 0 && ((input>>(8+worst_assign))&1) == 1)
          || (worst_assign > 0 && ((input>>(8-worst_assign))&1) == 0)) {
        fprintf(stdout, " (ok)\n");
        valid_bytes++;
      } else {
        fprintf(stdout, " (not ok)\n");
        invalid_bytes++;
      }
      assignements[abs(worst_assign)-1] = true;
      fix_value(cnf, -worst_assign);
    }
    free_word(target_hash, 256);
    free_word(hashed, 256);
    del_cnf(cnf);
    input++;
  } while (input != 0);
  fprintf(stdout, "=> %i / %i\n", valid_bytes, valid_bytes+invalid_bytes);
  return EXIT_SUCCESS;
}
