#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int numChoice()
{
    int num;
    printf("Enter number: ");
    scanf("%d", &num);

    return num;
}

char opChoice()
{
    char op;
    printf("Enter operator: ");
    scanf(" %c", &op); // Needs to put a space between " and % to register a character

    return op;
}


int main(void)
{
    int num1;
    int num2;
    char op;

    num1 = numChoice();
    num2 = numChoice();
    op = opChoice();

    if (op == '+')
    {
        printf("%d", num1 + num2);
    }
    else if (op == '-')
    {
        printf("%d", num1 - num2);
    }
    else if (op == '/')
    {
        printf("%d", num1 / num2);
    }
    else if (op == '*')
    {
        printf("%d", num1 * num2);
    }
    else
    {
        printf("Invalid Operator\n");
    }

}