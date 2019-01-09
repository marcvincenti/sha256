#ifndef GRAPH_H
#define GRAPH_H

typedef enum { constant, and, or, not } clause;

typedef enum { false = 0, true = 1 } bool;

typedef struct node_t {
  clause type;
  int nb_childs;
  union {
      /* for monoids */
      bool value;
      /* for non monoids */
      struct {
        int nb_parents;
        struct node_t ** parents;
      } parents;
  } data;
} node;

node* new_constant(bool);
void free_node(node*);

node* not1(node*);
node* and2(node*, node*);
node* or2(node*, node*);
node* or3(node*, node*, node*);
node* xor2(node*, node*);
node* xor3(node*, node*, node*);

bool get_val(node*);

#endif
