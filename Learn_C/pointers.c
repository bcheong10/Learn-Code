#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    // A pointer can be treated as another datatype
    int age = 30;
    int * pAge = &age; // Storing the memory address of 'int age' in the pointer variable 'pAge' -> physical memory of age
    
    double gpa = 3.73;
    double * pGpa = &gpa;

    char grade = 'A';
    char * pGrade = &grade;

    printf("age's memory address: %p", pAge);
    return 0;
}