#include <iostream>

using namespace std;

int main()
{   
    int age = 23;
    double gpa = 4.0;
    string name = "Ben";

    int *pAge = &age;   
    double *pGpa = &gpa;
    string *pName = &name;

    cout <<"The memory address of age: " << &age << endl; // Both works
    cout <<"The memory address of age: " << pAge << endl; // Using pointer variable

    // Dereferncing pointer - Goes back to the value instead of memory address
    cout << *pAge << endl; // Both works
    cout << *&age << endl;

    return 0;
}