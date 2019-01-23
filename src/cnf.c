#include <stdlib.h>
#include "../include/cnf.h"

value* new_boolean(boolean b) {
  value* v = malloc(sizeof(value));
  v->type = constant;
  v->value.b = b;
  return v;
}

value* new_litteral(cnf* c) {
  value* v = malloc(sizeof(value));
  v->type = variable;
  v->value.l = c->nb_litterals++;
  return v;
}

cnf* new_cnf() {
  cnf* c = malloc(sizeof(cnf));
  c->nb_litterals = 0;
  c->head = NULL;
  return c;
}

void new_clause(cnf* c, litteral l_a, litteral l_b, litteral l_c) {
  clause* cl = malloc(sizeof(clause));
  cl->litterals[0] = l_a;
  cl->litterals[1] = l_b;
  cl->litterals[2] = l_c;
  cl->next = c->head;
  c->head = cl;
}

void del_cnf(cnf* c) {
  if (c->head) {
    del_clause(c->head);
  }
  free(c);
}

void del_clause(clause* cl) {
  if (cl->next) {
    del_clause(cl->next);
  }
  free(cl);
}
