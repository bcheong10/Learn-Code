#include <stdio.h>

// Lecture 2: Data Types

int main()
{
    int integer = 10;
    
    double gpa = 3.0; // Double is a data type that can represent decimal number
    
    char character = 'B'; // Char must store characters in single quotations ' '

    char string[] = "Hello"; // Making a string using an array of char

    printf("500\n"); // Data type of '500' is a string
    printf("%d\n", 500); // Data type of '500' is an integer

    printf("My favorite %s is %d and %f\n", "number", 10, 10.0);

    const int NUM = 10; // "const" makes a variable unmodifiable

    return 0;

}