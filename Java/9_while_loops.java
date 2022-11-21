class while_loops
{
    public static void main(String[] args)
    {
        int x = 5;
        int multiplier = 1;
        int y = 1;

        // While loop
        while (multiplier <= 10)
        {
            System.out.printf("%d x %d = %d\n", multiplier, x, multiplier*x);
            multiplier ++;
        }

        // Do while loop
        do
        {
            System.out.printf("%d x %d = %d\n", y, x, y*x);
            y ++;
        } while (y <= 10);
    }
}