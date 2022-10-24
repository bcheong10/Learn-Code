#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    int age = 30;
    int * pAge = &age;

    printf("Memory address of 'age': %p\n", pAge);
    printf("Value inside memory address of 'age': %d", *pAge); // Putting * infront of a pointer dereferences it and returns the value that is stored in that memory address

    return 0;
}