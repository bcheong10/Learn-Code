import java.util.Scanner;

class input
{
    public static void main(String[] args) 
    {   
        // Creates a Scanner object (input) object
        Scanner scanner = new Scanner(System.in);

        // Series of input 
        System.out.print("Enter your name: ");
        String name = scanner.nextLine();

        System.out.print("Enter your age: ");
        int age = scanner.nextInt();

        // Clean ups the nextLine() buffer by reading <enter> in the previous nextIn() method
        scanner.nextLine();

        System.out.print("What programming language do you use: ");
        String language = scanner.nextLine();

        System.out.printf("Your name is %s, you are %d years old, you are using %s language", name, age, language);

        // Closes the Scanner object after use
        scanner.close();

    }
}