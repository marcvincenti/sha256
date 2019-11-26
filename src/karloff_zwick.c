#include <stdlib.h>
#include "../include/karloff_zwick.h"

__uint64_t count_clauses(cnf* cnf) {
  clause* cl = cnf->head;
  int count = 0;
  while (cl != NULL) {
    count++;
    cl = cl->next;
  }
  return count;
}

litteral pick_random_litteral(cnf* cnf) {
  clause* cl = cnf->head;
  if (cl != NULL) {
    if (cl->litterals[0] != 0) {
      return cl->litterals[0];
    } else if (cl->litterals[1] != 0) {
      return cl->litterals[1];
    } else if (cl->litterals[2] != 0) {
      return cl->litterals[2];
    }
  }
  return 0;
}

kz_value test_litteral(cnf* cnf, litteral l) {
  clause* cl = cnf->head;
  kz_value res;
  res.nb_sat = res.nb_unsat = 0;
  while (cl != NULL && cl->max_litteral >= abs(l)) {
    if (cl->litterals[0] == l || cl->litterals[1] == l || cl->litterals[2] == l) {
      /* We satisfy the clause */
      res.nb_sat++;
    }
    if (cl->litterals[0] == -l || cl->litterals[1] == -l || cl->litterals[2] == -l) {
      /* We unsatisfy the clause */
      res.nb_unsat++;
    }
    cl = cl->next;
  }
  return res;
}

kz_value karloff_zwick(cnf* cnf) {
  litteral l = pick_random_litteral(cnf);
  kz_value temp, final;
  final.nb_sat = 0;
  final.nb_unsat = count_clauses(cnf);
  while (l != 0) {
    temp = test_litteral(cnf, l);
    if (temp.nb_sat >= temp.nb_unsat) {
      fix_value(cnf, l);
      final.nb_sat += temp.nb_sat;
    } else {
      fix_value(cnf, -l);
      final.nb_sat += temp.nb_unsat;
    }
    l = pick_random_litteral(cnf);
  }
  final.nb_unsat -= final.nb_sat;
  return final;
}
