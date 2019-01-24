#include <stdlib.h>
#include <string.h>
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
  v->value.l = ++(c->nb_litterals);
  return v;
}

cnf* new_cnf() {
  cnf* cnf = malloc(sizeof(cnf));
  cnf->nb_litterals = 0;
  cnf->head = NULL;
  return cnf;
}

void new_clause(cnf* cnf, litteral l_a, litteral l_b, litteral l_c) {
  clause* cl = malloc(sizeof(clause));
  cl->litterals[0] = l_a;
  cl->litterals[1] = l_b;
  cl->litterals[2] = l_c;
  cl->next = cnf->head;
  cnf->head = cl;
}

void del_cnf(cnf* cnf) {
  clause* current;
  clause* next = cnf->head;
  while (next != NULL) {
    current = next;
    next = next->next;
    free(current);
  }
  free(cnf);
}

value* not(cnf* cnf, value* a) {
  value* r;
  if (a->type == constant) {
    if (a->value.b == false) {
      return new_boolean(true);
    } else {
      return new_boolean(false);
    }
  } else {
    r = memcpy(malloc(sizeof(value)), a, sizeof(value));
    r->value.l = -r->value.l;
    return r;
  }
}

value* or(cnf* cnf, value* a, value* b) {
  value* r;
  if (a->type == constant && b->type == constant) {
    return new_boolean(a->value.b || b->value.b);
  } else if (a->type == constant) {
    if (a->value.b == true) {
      return a;
    } else {
      return b;
    }
  } else if (b->type == constant) {
    if (b->value.b == true) {
      return b;
    } else {
      return a;
    }
  } else {
    /* a V b -> (¬r V a V b) & (r V ¬a) & (r V ¬b) */
    r = new_litteral(cnf);
    new_clause(cnf, -r->value.l, a->value.l, b->value.l);
    new_clause(cnf, r->value.l, -a->value.l, 0);
    new_clause(cnf, r->value.l, -b->value.l, 0);
    return r;
  }
}

value* and(cnf* cnf, value* a, value* b) {
  value* r;
  if (a->type == constant && b->type == constant) {
    return new_boolean(a->value.b && b->value.b);
  } else if (a->type == constant) {
    if (a->value.b == true) {
      return b;
    } else {
      return a;
    }
  } else if (b->type == constant) {
    if (b->value.b == true) {
      return a;
    } else {
      return b;
    }
  } else {
    /* a & b -> (r V ¬a V ¬b) & (¬r V a) & (¬r V b) */
    r = new_litteral(cnf);
    new_clause(cnf, r->value.l, -a->value.l, -b->value.l);
    new_clause(cnf, -r->value.l, a->value.l, 0);
    new_clause(cnf, -r->value.l, b->value.l, 0);
    return r;
  }
}

value* xor(cnf* cnf, value* a, value* b) {
  value* r;
  if (a->type == constant && b->type == constant) {
    return new_boolean(a->value.b ^ b->value.b);
  } else if (a->type == constant) {
    if (a->value.b == true) {
      return not(cnf, b);
    } else {
      return b;
    }
  } else if (b->type == constant) {
    if (b->value.b == true) {
      return not(cnf, a);
    } else {
      return a;
    }
  } else {
    /* a ^ b -> (a V b V ¬r) & (a V ¬b V r) & (¬a V b V r) & (¬a V ¬b V ¬r) */
    r = new_litteral(cnf);
    new_clause(cnf, -r->value.l, a->value.l, b->value.l);
    new_clause(cnf, -r->value.l, -a->value.l, -b->value.l);
    new_clause(cnf, r->value.l, -a->value.l, b->value.l);
    new_clause(cnf, r->value.l, a->value.l, -b->value.l);
    return r;
  }
}
