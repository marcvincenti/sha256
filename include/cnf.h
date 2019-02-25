#ifndef CNF_H
#define CNF_H

#include <stdint.h>

typedef enum { false = 0, true = 1 } boolean;

typedef __int32_t litteral;

union value_u {
   litteral l;
   boolean b;
};

typedef struct value_t {
  int nb_references;
  enum { constant, variable } type;
  union value_u value;
} value;

typedef struct clause_t {
  litteral litterals[4];
  litteral max_litteral;
  struct clause_t * next;
} clause;

typedef struct cnf_t {
  litteral nb_litterals;
  clause * head;
} cnf;

value* new_boolean(boolean);
value* new_litteral(cnf*);
value** copy_word(value**, value**, int);
void free_word(value**, int);

cnf* new_cnf();
cnf* copy_cnf(cnf*);
cnf* fix_value(cnf*, litteral);
void del_cnf(cnf*);

value* not(cnf*, value*);
value* or(cnf*, value*, value*);
value* and(cnf*, value*, value*);
value* xor(cnf*, value*, value*);
value* xor_3(cnf*, value*, value*, value*);
value* ch(cnf*, value*, value*, value*);
value* maj(cnf*, value*, value*, value*);

#endif
