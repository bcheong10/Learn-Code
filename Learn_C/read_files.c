#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{   
    char line[225];

    FILE * fpointer = fopen("employees.txt", "r");

    // Function that stores first line of file in variable
    // fgets(variable to store fist line, size, pointer of file
    fgets(line, 255, fpointer); // Reads 1st line of file
    printf("%s", line);

    // fpointer reads the next line of the file after subsequent read
    fgets(line, 255, fpointer); // Reads 2nd line of file
    printf("%s", line);

    fclose(fpointer);

    return 0;
}