#include <iostream>
#include <cmath> // Importing libraries for math functions

using namespace std;
  
int main()
{
    int age;
    cout << "Enter your age: ";

    cin >> age; // "cin" takes input from user and stores into variable 'age'
    cout << "You are " << age << " years old" << endl;

    // Inputting a string
    string name;
    cout << "Enter your name: ";
    getline(cin, name); // Function for user to input a string. Does not work at the same time as cin >>

    cout << "Hello " << name << endl;
}