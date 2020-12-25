/*
This is traditional CORDIC computation of sine and cosine.
The current code is based on [FXT: cordic-circ-demo.cc]
Correctly calculates cos and sine between 0-90 degrees (0-100).

INPUT:
	double theta: Input angle 
	long n: Number of iterations. 
OUTPUT:
	double &s: Reference to the sine part
	double &c: Reference to the cos part 

	error_sin= [abs(s-zs)/zs]*100;
	error_cos= [abs(c-zc)/zc]*100;
	Total_Error_Sin = sum(error_sin)
	Total_error_Cos = sum(error_cos)

*/
#include <math.h>
#include "prefixsum.h"
#include <stdio.h>
#include <stdlib.h>

using namespace std;

#define SIZE 128

int main(int argc, char **argv)
{	
	int fail = 0;
	int in[SIZE];
	int out[SIZE], out_sw[SIZE];
	for(int i = 0; i < SIZE; i++) {
		in[i] = i;
	}
	prefixsum_sw(in, out_sw);
	prefixsum_hw(in, out);
	// prefixsum_bo(in, out);
	// prefixsum_unroll(in, out);
	// prefixsum_op(in, out);
	for(int i = 0; i < SIZE; i++) {
		if(out_sw[i]!=out[i]){
			fail = 1;
		}
		// printf("%d \n", out[i]);
	}
	// printf("\n");

	if(fail == 1)
		printf("FAILED\n");
	else
		printf("PASS\n");

	return fail;
}
