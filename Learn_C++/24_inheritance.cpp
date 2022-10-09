#include <iostream>

using namespace std;

// Superclass
class Chef 
{
    public:
        void makeChicken() {
            cout << "The chef is making chicken..." << endl;
        }
        void makeSalad() {
            cout << "The chef is making salad..." << endl;
        }
        void makeSpecial() {
            cout << "The chef is making bbq rice" << endl;
        }
};

// Subclass
class ItalianChef : public Chef // "ItalianChef" inherits from "Chef" class
{
    public:
        void makePasta(){
            cout << "The chef is making pasta..." << endl;
        }
};

int main()
{
    Chef chef;
    chef.makeChicken();

    ItalianChef italianChef;
    italianChef.makePasta();

    return 0;
}
