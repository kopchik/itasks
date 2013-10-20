#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>

int main(void) {
  char a[10];
  printf("%ld\n", &a[1]-&a[0]);
  return 0;
}
