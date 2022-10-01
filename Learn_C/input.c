#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    // int age;
    // printf("Enter age: ");
    // scanf("%d\n", &age); // %d only accepts input as an integer. &age stores the input into the variable "age"
    // printf("You are %d years old\n", age);

    char name[20];
    printf("Enter your name: ");
    // scanf("%s", name); // No need to put '&' if getting a string input
    fgets(name, 20, stdin); // fgets(variable, no. of char, library). Function is able to store a line of string. 
    // fgets() does not work after scanf() 
    printf("Your name is: %s", name);

    return 0;
}