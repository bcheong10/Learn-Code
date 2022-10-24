#include <iostream>

using namespace std;

// Creating a class
class Book
{
    // Listing all attributes of the class
    public:
        string title;
        string author;
        int pages;

        // Constructor - Function that gets called whenever an object of this class is created
        Book(string aTitle, string aAuthor, int aPages) // Allows for input of argument when object is created
        {
            title = aTitle;
            author = aAuthor;
            pages = aPages;
           
        }
};

int main()
{
    Book book1("Harry Potter", "Jk Rowling", 500); // Calls the constructor
    Book book2("Lord of the Rings", "Tolkein", 700); 
    
    cout << book1.title << endl;
    cout << book2.title << endl;

}