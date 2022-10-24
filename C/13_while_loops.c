#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    int index = 1;
    
    do
    {
        printf("%d\n", index);
        index++;
    }
    while (index <= 5);

    return 0;
}