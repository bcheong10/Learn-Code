#include <stdio.h>
#include <stdlib.h>
#include <string.h>

double cube();

int main()
{
    printf("Answer: %f", cube(2));
    
    return 0;
}

double cube(int num)
{
    double result = num * num * num;
    
    return result;
}