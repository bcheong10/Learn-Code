#include <iostream>

using namespace std;

class Movie
{
    // Makes the public unable to access .rating function
    private:
        string rating;

    // Everything under public can be accessed
    public:
        string title;
        string director;

        Movie(string aTitle, string aDirector, string aRating)
        {
            title = aTitle;
            director = aDirector;
            rating = aRating;
        }

        void setRating(string aRating)
        {
            if (aRating == "G" || aRating == "PG" || aRating == "R") // Set condition for using this function
            {
                rating = aRating;
            }
            else
            {
                rating = "NR";
            }
        }

        string getRating()
        {
            return rating;
        }

};

int main()
{
    Movie avengers("The Avengers", "Joss Whedon", "PG");

    avengers.setRating("Dog");
    cout << avengers.getRating();
}