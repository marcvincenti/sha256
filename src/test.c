#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "../include/cnf.h"
#include "../include/hash.h"

boolean satisfy(char* assignment, litteral l) {
  if (l != 0 && assignment[abs(l)] != 0 && (assignment[abs(l)] > 0) == (l > 0)) {
    return true;
  } else {
    return false;
  }
}

boolean unsatisfy(char* assignment, litteral l) {
  if (l == 0 || (assignment[abs(l)] != 0 && (assignment[abs(l)] > 0) != (l > 0))) {
    return true;
  } else {
    return false;
  }
}

boolean propagate_assignment(cnf* cnf, char* assignment) {
  int new_assignments;
  clause* cl;
  do {
    new_assignments = 0;
    cl = cnf->head;
    while (cl != NULL) {
      /* if not satisfied */
      if (!satisfy(assignment, cl->litterals[0])
      && !satisfy(assignment, cl->litterals[1])
      && !satisfy(assignment, cl->litterals[2])
      && !satisfy(assignment, cl->litterals[3])) {
        /* If one possible, set new assignment */
        if(cl->litterals[0] != 0 && assignment[abs(cl->litterals[0])] == 0
          && unsatisfy(assignment, cl->litterals[1])
          && unsatisfy(assignment, cl->litterals[2])
          && unsatisfy(assignment, cl->litterals[3])) {
          assignment[abs(cl->litterals[0])] = cl->litterals[0] < 0 ? -1 : 1;
          new_assignments++;
        } else if (cl->litterals[1] != 0 && assignment[abs(cl->litterals[1])] == 0
                  && unsatisfy(assignment, cl->litterals[0])
                  && unsatisfy(assignment, cl->litterals[2])
                  && unsatisfy(assignment, cl->litterals[3])) {
          assignment[abs(cl->litterals[1])] = cl->litterals[1] < 0 ? -1 : 1;
          new_assignments++;
        } else if (cl->litterals[2] != 0 && assignment[abs(cl->litterals[2])] == 0
                  && unsatisfy(assignment, cl->litterals[0])
                  && unsatisfy(assignment, cl->litterals[1])
                  && unsatisfy(assignment, cl->litterals[3])) {
          assignment[abs(cl->litterals[2])] = cl->litterals[2] < 0 ? -1 : 1;
          new_assignments++;
        }else if (cl->litterals[3] != 0 && assignment[abs(cl->litterals[3])] == 0
                  && unsatisfy(assignment, cl->litterals[0])
                  && unsatisfy(assignment, cl->litterals[1])
                  && unsatisfy(assignment, cl->litterals[2])) {
          assignment[abs(cl->litterals[3])] = cl->litterals[3] < 0 ? -1 : 1;
          new_assignments++;
        } else if (unsatisfy(assignment, cl->litterals[0])
                  && unsatisfy(assignment, cl->litterals[1])
                  && unsatisfy(assignment, cl->litterals[2])
                  && unsatisfy(assignment, cl->litterals[3])) {
          /* If non-possible, send false */
          return false;
        }
      }
      cl = cl->next;
    }
  } while (new_assignments > 0);
  return true;
}

int main (int argc, char* argv[]) {
  int i;
  value** hashed;
  cnf* cnf;
  char* assignment;
  if (argc == 2) {
    cnf = new_cnf();
    hashed = hash(cnf, "", strlen(argv[1]) << 3);
    assignment = malloc(sizeof(char) * (cnf->nb_litterals + 1));
    /* assign entries */
    memset(assignment, 0, sizeof(char) * (cnf->nb_litterals + 1));
    for (i = 0; i < strlen(argv[1]); i++) {
      assignment[(i<<3)+1] = (argv[1][i] & 128) ? 1 : -1;
      assignment[(i<<3)+2] = (argv[1][i] &  64) ? 1 : -1;
      assignment[(i<<3)+3] = (argv[1][i] &  32) ? 1 : -1;
      assignment[(i<<3)+4] = (argv[1][i] &  16) ? 1 : -1;
      assignment[(i<<3)+5] = (argv[1][i] &   8) ? 1 : -1;
      assignment[(i<<3)+6] = (argv[1][i] &   4) ? 1 : -1;
      assignment[(i<<3)+7] = (argv[1][i] &   2) ? 1 : -1;
      assignment[(i<<3)+8] = (argv[1][i] &   1) ? 1 : -1;
    }
    /* propagate and display solution */
    if (propagate_assignment(cnf, assignment) == true) {
      for (i = 0; i < 256; i++) {
        if (hashed[i]->type == variable) {
          if (assignment[abs(hashed[i]->value.l)] == 1) {
            if (hashed[i]->value.l > 0) {
              fprintf(stdout, "1");
            } else {
              fprintf(stdout, "0");
            }
          } else if (assignment[abs(hashed[i]->value.l)] == -1) {
            if (hashed[i]->value.l > 0) {
              fprintf(stdout, "0");
            } else {
              fprintf(stdout, "1");
            }
          }
        } else {
          if (assignment[hashed[i]->value.b]) {
            fprintf(stdout, "1");
          } else {
            fprintf(stdout, "0");
          }
        }
      }
      fprintf(stdout, "\n");
    } else {
      fprintf(stdout, "The cnf and assignment provided doesn't accept a solution.\n");
    }
    free(assignment);
    free(hashed);
    del_cnf(cnf);
    return EXIT_SUCCESS;
  } else {
    fprintf(stderr, "illegal usage of %s\n", argv[0]);
    fprintf(stderr, "usage: %s [message]\n", argv[0]);
    return EXIT_FAILURE;
  }
}
