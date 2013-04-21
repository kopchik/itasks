#include <stdlib.h>
#include <stdio.h>

static int A[2][2]=
  {
    {1, 2},
    {3, 4},
  };

static int B[2][2]=
  {
    {4, 3},
    {2, 1},
  };

static int C[2][2];

int main(void) {
  for (int row=0; row<2; row++) {
    for (int col=0; col<2; col++) {
      for (int k=0; k<2; k++) {
        C[row][col] += A[row][k]*B[k][col];
      }
    }
  }

  printf("%d %d\n", C[0][0], C[0][1]);
  printf("%d %d\n", C[1][0], C[1][1]);
}
