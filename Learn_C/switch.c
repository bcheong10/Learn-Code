#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    char grade = 'A';

    switch(grade) // Switch checks the variable inside and outputs according to the cases
    {
        case 'A':
            printf("You did great!");
            break;
        case 'B': 
            printf("You did alright");
            break;
        case 'C':
            printf("You did poorly");
            break;
        default: // Default when variable is invalid
            printf("Invalid grade");

    }

    return 0;
}