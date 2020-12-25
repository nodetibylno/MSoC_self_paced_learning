// The file cordic.h holds definitions for the data types and constant values
#include "prefixsum.h"
#define SIZE 128

void prefixsum_sw(int in[SIZE], int out[SIZE])
{
	out[0] = in[0];
	for(int i=1; i < SIZE; i++) {
		out[i] = out[i-1] + in[i];
	}
}
