#include <iostream>

using namespace std;

int main()
{
    int array[3][2] = {
                        {1, 2},
                        {3, 4},
                        {5, 6}
                    };
        
    cout << array[2][1] << endl; // Access individual values in 2d array

    // Nested for loops
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 2; j++)
        {
            cout << array[i][j] << " ";
        }
        cout << endl;
    }
            
}