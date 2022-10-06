#include <iostream>

using namespace std;

int main()
{
    string phrase = "chicken";
    cout << phrase.length() << endl; // Length function
    cout << phrase[0] << endl; // Accessing specific index
    
    phrase[0] = 'B';
    cout << phrase[0] << endl;

    cout << phrase.find("ken", 0) << endl; // .find(string, no. of index to start looking)

    string substring = phrase.substr(0, 5); //.substr(first undex to extract, second in dex to extrac)
    cout << subtring << endl;

}