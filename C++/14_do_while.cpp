#include <iostream>

using namespace std;

int main()
{
    int index = 10;

    do
    {
        cout << index << endl; // This line is still executed as it runs first, then the code checks the while loop condition
    }
    while (index < 10);
}