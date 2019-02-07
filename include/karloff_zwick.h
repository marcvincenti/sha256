#ifndef KZ_H
#define KZ_H

#include "./cnf.h"

typedef struct kz_value_t {
  __uint64_t nb_sat;
  __uint64_t nb_unsat;
} kz_value;

kz_value karloff_zwick(cnf*);

#endif
