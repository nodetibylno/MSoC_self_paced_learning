
#ifndef PREFIXSUM_H
#define PREFIXSUM_H

const static int SIZE = 128;

void prefixsum_sw(int in[SIZE], int out[SIZE]);
void prefixsum_hw(int in[SIZE], int out[SIZE]);
void prefixsum_bo(int in[SIZE], int out[SIZE]);
void prefixsum_unroll(int in[SIZE], int out[SIZE]);
void prefixsum_op(int in[SIZE], int out[SIZE]);

#endif
