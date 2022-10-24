#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int Numbers[] = {1, 5, 10, 15};
    Numbers[0] = 7; // Modifying existing arrays

    cout << Numbers[0] << endl;

    return 0;
}