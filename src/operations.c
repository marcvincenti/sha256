#include <stdlib.h>
#include "../include/operations.h"

/*
 * Process a 32bits addition
 */
node** bool_add_32(node** a, node** b) {
  int i;
  node* r;
  node** res = malloc(sizeof(node*) * 32);
  r = and2(a[31], b[31]);
  res[31] = xor2(a[31], b[31]);
  /* res[31] = new_constant(get_val(a[31]) ^ get_val(b[31])); */
  for (i = 30; i >= 0; i--) {
    res[i] = xor3(a[i], b[i], r);
    /* res[i] = new_constant(get_val(a[i]) ^ get_val(b[i]) ^ get_val(r)); */
    if (i != 0) {
      r = or3(and2(a[i], b[i]), and2(a[i], r), and2(b[i], r));
    }
  }
  return res;
}

/*
 * Process a S0 word function
 */
node** bool_s_0(node** x) {
  int i = 0;
  node** res = malloc(sizeof(node*) * 32);
  for (; i < 3; i++) {
    res[i] = xor2(x[(i-7)&31], x[(i-18)&31]);
  }
  for (; i < 32; i++) {
    res[i] = xor3(x[(i-7)&31], x[(i-18)&31], x[i-3]);
  }
  return res;
}

/*
 * Process a S1 word function
 */
node** bool_s_1(node** x) {
  int i = 0;
  node** res = malloc(sizeof(node*) * 32);
  for (; i < 10; i++) {
    res[i] = xor2(x[(i-17)&31], x[(i-19)&31]);
  }
  for (; i < 32; i++) {
    res[i] = xor3(x[(i-17)&31], x[(i-19)&31], x[i-10]);
  }
  return res;
}

/*
 * Process a E0 word function
 */
node** bool_e_0(node** x) {
  int i = 0;
  node** res = malloc(sizeof(node*) * 32);
  for (; i < 32; i++) {
    res[i] = xor3(x[(i-2)&31], x[(i-13)&31], x[(i-22)&31]);
  }
  return res;
}

/*
 * Process a E1 word function
 */
node** bool_e_1(node** x) {
  int i = 0;
  node** res = malloc(sizeof(node*) * 32);
  for (; i < 32; i++) {
    res[i] = xor3(x[(i-6)&31], x[(i-11)&31], x[(i-25)&31]);
  }
  return res;
}

/*
 * Process a Ch word function
 */
node** bool_ch(node** x, node** y, node** z) {
  int i = 0;
  node** res = malloc(sizeof(node*) * 32);
  for (; i < 32; i++) {
    res[i] = or2(and2(x[i], y[i]), and2(not1(x[i]), z[i]));
  }
  return res;
}

/*
 * Process a Maj word function
 */
node** bool_maj(node** x, node** y, node** z) {
  int i = 0;
  node** res = malloc(sizeof(node*) * 32);
  for (; i < 32; i++) {
    res[i] = or3(and2(x[i], y[i]), and2(x[i], z[i]), and2(y[i], z[i]));
  }
  return res;
}
