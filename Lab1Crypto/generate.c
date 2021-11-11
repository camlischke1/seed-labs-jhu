#define LEN 32 // 128 bits
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

void bin(unsigned n);

int main(){
char binary[256];
int i;
unsigned char *key = (unsigned char *) malloc(sizeof(unsigned char)*LEN);
FILE* random = fopen("/dev/urandom", "r");
fread(key, sizeof(unsigned char)*LEN, 1, random);
fclose(random);

for (i = 0; i< LEN; i++){
//printf("%.2x", (unsigned char)key[i]);
bin((unsigned char)key[i]);
printf("%s ",binary);
}


return 0;
}


void bin(unsigned n)
{
    unsigned i;
    for (i = 1 << 7; i > 0; i = i / 2)
        (n & i) ? printf("1") : printf("0");
}
