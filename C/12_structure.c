#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Student
{
    char name[50];
    char major[50];
    int age;
    double gpa;
};

int main()
{
    struct Student student1;
    student1.age = 23;
    student1.gpa = 3.73;
    strcpy(student1.name, "Ben"); // strcpy stores a string (array of characters) into a variable
    strcpy(student1.major, "EEE");

    struct Student student2;
    student1.age = 22;
    student1.gpa = 3.2;
    strcpy(student2.name, "George"); 
    strcpy(student2.major, "MAE");

    printf("%s\n", student1.name);
    printf("%f\n", student1.gpa);

    return 0;
}