#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "../include/karloff_zwick.h"
#include "../include/hash.h"

/* validation seuil
"" 1 byte => 0.029461
"" 2 bytes => 0.029344
"" 3 bytes => 0.029433
"" 4 bytes => 0.029502
"0xDEADBEEF" 1 byte => 0.029394
"0xDEADBEEF" 2 bytes => 0.029441
"0xDEADBEEF" 3 bytes => 0.029460
"0xDEADBEEF" 4 bytes => 0.029462
"0xC0FFEE" 1 byte => 0.029501
"0xC0FFEE" 2 bytes => 0.029457
"0xC0FFEE" 3 bytes => 0.029440
"0xC0FFEE" 4 bytes => 0.029481
"0xBADF00D" 1 byte => 0.029329
"0xBADF00D" 2 bytes => 0.029497
"0xBADF00D" 3 bytes => 0.029566
"0xBADF00D" 4 bytes => 0.029590
"0xFEEDC0DE" 1 byte => 0.029447
"0xFEEDC0DE" 2 bytes => 0.029467
"0xFEEDC0DE" 3 bytes => 0.029480
"0xFEEDC0DE" 4 bytes => 0.029548
*/
#define WORST_VALIDATION 0.029600

int main (int argc, char* argv[]) {
  int i, j, k;
  cnf* cnf;
  value** hashed;
  kz_value res;
  char* prefix = "0xDEADBEEF";
  double approx;
  for (i = 1; i < 5; i++) {
    fprintf(stdout, "===== { prefix: \"%s\", nonce: %i bytes } =====\n", prefix, i);
    for (j = 1; j <= 64; j++) {
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
      approx = (double)res.nb_unsat / (res.nb_unsat+res.nb_sat);
      if (approx <=  WORST_VALIDATION) {
        fprintf(stdout, " => OK");
      } else {
        fprintf(stdout, " => NOT OK");
      }
      fprintf(stdout, " (%f)\n", approx);
      free_word(hashed, 256);
      del_cnf(cnf);
    }
    fprintf(stdout, "\n");
  }
  return EXIT_SUCCESS;
}
