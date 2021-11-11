/* stack.c */
/* Modified by Tushar Jois for JHU 601.443/643, Security and Privacy. */
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#define MAX_SIZE 100000
int bof(char *str)
{
char buffer[100];
unsigned short len = strlen(str);
if (len >= 100) {
return 0;
}
strncpy(buffer, str, strlen(str));
return 1;
}
int main(int argc, char **argv)
{
char str[MAX_SIZE];
FILE *badfile;
badfile = fopen("badfile", "r");
fread(str, sizeof(char), MAX_SIZE, badfile);
if (bof(str)) {
printf("Returned Properly\n");
return 0;
}
return 443;
}
