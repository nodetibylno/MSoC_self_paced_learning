// The file cordic.h holds definitions for the data types and constant values
#include "prefixsum.h"
#define SIZE 128

void prefixsum_hw(volatile int in[SIZE], volatile int out[SIZE])
{
	int in_buf[SIZE], out_buf[SIZE];
#pragma HLS ARRAY_PARTITION variable=out_buf cyclic factor=4 dim=1
#pragma HLS ARRAY_PARTITION variable=in_buf cyclic factor=4 dim=1

	for(int i=0; i < SIZE; i++) {
#pragma HLS PIPELINE
		in_buf[i] = in[i];
	}

	int A = in_buf[0];
	for(int i=0; i < SIZE; i++) {
#pragma HLS UNROLL factor=4
#pragma HLS PIPELINE
		A = A + in_buf[i];
		out_buf[i] = A;
	}

	for(int i=0; i < SIZE; i++) {
#pragma HLS PIPELINE
			out[i] = out_buf[i];
		}
}
