#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "../include/graph.h"

node* new_clause(clause type, int nb_parents, node** parents) {
int i;
  node* n = malloc(sizeof(node));
  n->type = type;
  n->nb_childs = 0;
  n->data.parents.nb_parents = nb_parents;
  if (nb_parents > 0) {
    n->data.parents.parents = malloc(sizeof(node*) * nb_parents);
    memcpy(n->data.parents.parents, parents, sizeof(node*) * nb_parents);
    for (i = 0; i < n->data.parents.nb_parents; i++) {
      n->data.parents.parents[i]->nb_childs++;
    }
  }
  return n;
}

node* new_constant(bool val) {
  node* n = malloc(sizeof(node));
  n->type = constant;
  n->nb_childs = 0;
  n->data.value = val;
  return n;
}

void free_node(node* node) {
  int i;
  if (node->type != constant) {
    for (i = 0; i < node->data.parents.nb_parents; i++) {
      if (node->data.parents.parents[i]->nb_childs <= 1) {
        free_node(node->data.parents.parents[i]);
      } else {
        node->data.parents.parents[i]->nb_childs--;
      }
    }
  }
  free(node);
}

node* not1(node* a) {
  return new_clause(not, 1, &a);
}

node* and2(node* a, node* b) {
  node* clauses[2];
  clauses[0] = a; clauses[1] = b;
  return new_clause(and, 2, clauses);
}

node* or2(node* a, node* b) {
  node* clauses[2];
  clauses[0] = a; clauses[1] = b;
  return new_clause(or, 2, clauses);
}

node* or3(node* a, node* b, node* c) {
  node* clauses[3];
  clauses[0] = a; clauses[1] = b; clauses[2] = c;
  return new_clause(or, 3, clauses);
}

node* xor2(node* a, node* b) {
  return or2(and2(a, not1(b)), and2(not1(a), b));
}

node* xor3(node* a, node* b, node* c) {
  node* clauses[4], * abc[3];
  node* not_a = not1(a);
  node* not_b = not1(b);
  node* not_c = not1(c);
  abc[0] = a; abc[1] = not_b; abc[2] = not_c;
  clauses[0] = new_clause(and, 3, abc);
  abc[0] = not_a; abc[1] = b;
  clauses[1] = new_clause(and, 3, abc);
  abc[1] = not_b; abc[2] = c;
  clauses[2] = new_clause(and, 3, abc);
  abc[0] = a; abc[1] = b;
  clauses[3] = new_clause(and, 3, abc);
  return new_clause(or, 4, clauses);
}

bool get_val(node* node) {
  int i; bool b;
  switch (node->type) {
    case constant:
      return node->data.value;
    case and:
      for (i = 0; i < node->data.parents.nb_parents; i++) {
        if (!get_val(node->data.parents.parents[i])) {
          return false;
        }
      }
      return true;
    case or:
      for (i = 0; i < node->data.parents.nb_parents; i++) {
        if (get_val(node->data.parents.parents[i])) {
          return true;
        }
      }
      return false;
    case not:
      return !get_val(node->data.parents.parents[0]);
    default:
    fprintf(stderr, "Unknown node type in get_val()\n");
      exit(EXIT_FAILURE);
  }
}
