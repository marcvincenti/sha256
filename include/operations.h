#ifndef OPERATIONS_H
#define OPERATIONS_H

#include "./cnf.h"

value** bool_add_32(cnf*, value**, value**);

value** bool_s_0(cnf*, value**);
value** bool_s_1(cnf*, value**);

value** bool_e_0(cnf*, value**);
value** bool_e_1(cnf*, value**);

value** bool_ch(cnf*, value**, value**, value**);
value** bool_maj(cnf*, value**, value**, value**);

#endif
