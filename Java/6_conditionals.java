import java.util.Scanner;

class conditionals
{
    public static void main(String[] args)
    {
        // Creating a calculator
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter first number: ");
        int number_1 = scanner.nextInt();
        scanner.nextLine();

        System.out.print("Enter second number: ");
        int number_2 = scanner.nextInt();
        scanner.nextLine();

        System.out.print("Enter arithmetic operation: ");
        String operation = scanner.nextLine();

        if (operation.equals("+"))
        {
            System.out.printf("Sum of %d and %d is %d", number_1, number_2, number_1 + number_2);
        }
        else if (operation.equals("-"))
        {
            System.out.printf("%d", number_1 - number_2);
        }

        scanner.close();
    }
}