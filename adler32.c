#include <stdlib.h>
#include <stdio.h>
#define BASE 65521UL
#define NMAX 5552
#define MOD(a) a %= BASE
typedef unsigned long  uLong;

uLong adler32(uLong adler, char *buf, size_t len)
{
    //uLong s1 = adler & 0xffff;
    //uLong s2 = (adler >> 16) & 0xffff;
    uLong s1=1, s2=0, answer;
    int k;
    while (len--) {
        s1 += *buf++;
        s2 += s1;
    }
    if (s1 >= BASE)
        s1 -= BASE;
    MOD(s2);             /* only added so many BASE's */
    answer =  (s2 << 16) | s1;
    printf("%lu %lu %lu\n", s1, s2, answer);
    return answer;
}


int main(void) {
  printf("%lu\n", adler32(65537, "\1\2", 2));
  printf("%lu\n", 2<<16);
}
