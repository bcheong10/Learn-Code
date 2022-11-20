class forLoops
{
    public static void main(String[] args)
    {
        // for(initialization; condition; increment)
        for (int i = 0; i < 5; i++)
        {
            System.out.println(i);
        }

        // Method 1: Loop through an array
        int numbers[] = {1, 4, 10, 12, 11};

        for (int index = 0; index < numbers.length; index++)
        {
            System.out.println(numbers[index]);
        }
        
        // Method 2: Loop through an array
        for (int number: numbers)
        {
            System.out.print(number + " ");
        }

    }
}