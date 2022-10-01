#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    char color[20];
    char plural[20];
    char celebrityFirst[20];
    char celebrityLast[20];

    printf("Enter a color: ");
    scanf("%s", color);

    printf("Enter a plural noun: ");
    scanf("%s", plural);

    printf("Enter celebrity: ");
    scanf("%s%s", celebrityFirst, celebrityLast); // Collects 2 words separated by a space

    printf("Roses are %s\n", color);
    printf("%s are blue\n", plural);
    printf("I love %s %s", celebrityFirst, celebrityLast);

    return 0;
}