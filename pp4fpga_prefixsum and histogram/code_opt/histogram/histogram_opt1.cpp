#include "histogram.h"
void histogram_opt(int in[INPUT_SIZE], int hist[VALUE_SIZE]) {

  int acc = 0;
  int i, val;
  int in_buf[INPUT_SIZE], hist_buf[VALUE_SIZE];

  for(i = 0; i < INPUT_SIZE; i++) {
#pragma HLS PIPELINE II=1
	  in_buf[i] = in[i];
  }

  int old = in_buf[0];

  loop0: for(i = 0; i < INPUT_SIZE; i++) {
#pragma HLS PIPELINE II=1
	val = in_buf[i];
    if(old == val) {
      acc = acc + 1;
    } else {
      hist_buf[old] = acc;
      acc = hist_buf[val] + 1;
    }
    old = val;
  }
  hist_buf[old] = acc;

  for(i = 0; i < VALUE_SIZE; i++) {
#pragma HLS PIPELINE II=1
  	   hist[i] = hist_buf[i];
    }

}
