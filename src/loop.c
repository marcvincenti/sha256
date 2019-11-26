#include <stdio.h>
#include <stdlib.h>
#include "../include/hash.h"

int main (int argc, char* argv[]) {
  int i;
  clause* cl;
  cnf* cnf = new_cnf();
  value** hashed = hash(cnf, "", 256);
  for (i = 0; i < 256; i++) {
    if (hashed[i]->type == variable) {
      new_clause(cnf, hashed[i]->value.l, -(i+1), 0);
      new_clause(cnf, -hashed[i]->value.l, (i+1), 0);
    } else {
      fprintf(stderr, "hashed[%i] is a constant.\n", i);
      EXIT_FAILURE;
    }
  }
  i = 0;
  cl = cnf->head;
  while(cl != NULL) {
    i++;
    cl = cl->next;
  }
  fprintf(stdout, "c ===== STRANGE-LOOP =====\n");
  fprintf(stdout, "p cnf %i %i\n", cnf->nb_litterals, i);
  cl = cnf->head;
  while(cl != NULL) {
    if (cl->litterals[0] != 0) {
      fprintf(stdout, "%i ", cl->litterals[0]);
    }
    if (cl->litterals[1] != 0) {
      fprintf(stdout, "%i ", cl->litterals[1]);
    }
    if (cl->litterals[2] != 0) {
      fprintf(stdout, "%i ", cl->litterals[2]);
    }
    fprintf(stdout, "0\n");
    cl = cl->next;
  }
  del_cnf(cnf);
  return EXIT_SUCCESS;
}
