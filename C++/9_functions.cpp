#include <iostream>
#include <cmath>

using namespace std;

void sayHi(string name, int age)
{
    cout << "Hello " << name << ", you are " << age << " years old" << endl;
}


int main()
{
    sayHi("Ben", 23);
    sayHi("Honk", 80);
    
    return 0;
}