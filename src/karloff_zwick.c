#include <stdlib.h>
#include "../include/karloff_zwick.h"

litteral pick_litteral(cnf* cnf) {
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
    } else if (cl->litterals[0] == -l) {
      if (cl->litterals[1] == 0 && cl->litterals[2] == 0) {
        /* We unsatisfy the clause */
        res.nb_unsat++;
      }
    } else if (cl->litterals[1] == -l) {
      if (cl->litterals[0] == 0 && cl->litterals[2] == 0) {
        /* We unsatisfy the clause */
        res.nb_unsat++;
      }
    } else if (cl->litterals[2] == -l) {
      if (cl->litterals[0] == 0 && cl->litterals[1] == 0) {
        /* We unsatisfy the clause */
        res.nb_unsat++;
      }
    }
    cl = cl->next;
  }
  return res;
}

kz_value karloff_zwick(cnf* cnf) {
  litteral l = pick_litteral(cnf);
  kz_value s1, s2, final;
  final.nb_sat = final.nb_unsat = 0;
  while (l != 0) {
    s1 = test_litteral(cnf, l);
    s2 = test_litteral(cnf, -l);
    if (((s1.nb_sat<<3)+(s1.nb_unsat*7)) >= ((s2.nb_sat<<3)+(s2.nb_unsat*7))) {
      fix_value(cnf, l);
      final.nb_sat += s1.nb_sat;
      final.nb_unsat += s1.nb_unsat;
    } else {
      fix_value(cnf, -l);
      final.nb_sat += s2.nb_sat;
      final.nb_unsat += s2.nb_unsat;
    }
    l = pick_litteral(cnf);
  }
  return final;
}
