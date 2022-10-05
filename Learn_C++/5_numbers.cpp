#include <iostream>
#include <cmath> // Importing libraries for math functions

using namespace std;

int main()
{
    cout << 10 % 3 << endl; // Modulus operator
    
    int num1 = 5;
    num1++;
    
    int num2 = 5;
    num2 -= 10;
    
    int num3 = 5;
    num3 /= 10;

    cout << num1 << endl;
    cout << num2 << endl;
    cout << num3 << endl;

    cout << pow(2, 5) << endl; // A cmath function
    cout << round(4.3) << endl; // Another cmath function

    return 0;
}