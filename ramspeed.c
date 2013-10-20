#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

#define SIZE 1000*1024*1024
int main(void) {
  char *A = malloc(SIZE);
  assert(A);

//  for (int i=0; i<SIZE; i++) {
//    A[i] = '0';
//  }
//  for (int j=0; j <10; j++) {
  for (int i=0; i<SIZE/sizeof(int); i=i+sizeof(int)) {
    A[i] = 0;
  }
//  }

  printf("===");
  int d;
  for (int j=0; j<1; j++) {
    for (int i=0; i<SIZE/sizeof(d); i=i+sizeof(d)) {
      d = (int) A[i];
    }
  }

  free(A);
}
