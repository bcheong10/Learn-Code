#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    int luckyNumbers[] = {5, 8, 10};
    luckyNumbers[0] = 11; // Overides the previous assignment
    printf("%d", luckyNumbers[0]);
    
    return 0;
}