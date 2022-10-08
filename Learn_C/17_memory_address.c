#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    int age = 23;
    double gpa = 3.73;
    char grade = 'A';

    printf("age: %p\n", &age); // Printing the memory address of the variables
    printf("gpa: %p\n", &gpa);
    printf("grade: %p\n", &grade);

    return 0;

}