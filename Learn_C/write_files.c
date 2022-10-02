#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    // Creates a pointer variable that points to the memory address of "employees.txt"
    // fopen("name of file", "file mode")
    // file mode - (r: read), (w: write), (a: append)
    FILE * fpointer = fopen("employees.txt", "w");

    // Writes information into the file that is open
    fprintf(fpointer, "Jim: Salesman\nOscar: Accounting\nDwight: Assistant Manager");

    fclose(fpointer);

    return 0;
}