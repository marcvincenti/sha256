#ifndef CNF_H
#define CNF_H

typedef enum { false = 0, true = 1 } boolean;

typedef __int32_t litteral;

union value_u {
   litteral l;
   boolean b;
};

typedef struct value_t {
  enum { constant, variable } type;
  union value_u value;
} value;

typedef struct clause_t {
  litteral litterals[3];
  litteral max_litteral;
  struct clause_t * next;
} clause;

typedef struct cnf_t {
  litteral nb_litterals;
  clause * head;
} cnf;

value* new_boolean(boolean);
value* new_litteral(cnf*);

cnf* new_cnf();
cnf* fix_value(cnf*, litteral);
void del_cnf(cnf*);

value* not(cnf*, value*);
value* or(cnf*, value*, value*);
value* or_3(cnf*, value*, value*, value*);
value* and(cnf*, value*, value*);
value* xor(cnf*, value*, value*);
value* xor_3(cnf*, value*, value*, value*);

#endif
