class data_types
{
    public static void main(String[] args)
    {   
        // Integer types
        byte aSingleByte = 100; // -128 to 127
        short aSmallNumber = 20000; 
        int anInteger = 21083081;
        long aLargeNumber = 908392813098238745L;

        // Decimal types
        double aDouble = 1.283910;
        float aFloat = 3.4020F;

        // Booleans
        boolean isTrue = true;
        boolean isFalse = false;

        // Characters
        char copyrightSymbol = '\u00A9';
        char percentSymbol = '%';

        System.out.println("This is the copyright symbol: " + copyrightSymbol);
        System.out.println("This is the percent symbol: " + percentSymbol);

    }
}