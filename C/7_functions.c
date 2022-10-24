#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void sayHello(); // Declare the function before int main()

int main()
{
    sayHello("Ben", 23);
    return 0;
}

// Function #1
void sayHello(char name[], int age)
{
    printf("Hello %s, you are %d years old", name, age);
}