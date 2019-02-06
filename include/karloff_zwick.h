#ifndef KZ_H
#define KZ_H

#include "./cnf.h"

typedef struct kz_value_t {
  int nb_sat;
  int nb_unsat;
} kz_value;

kz_value karloff_zwick(cnf*);

#endif
