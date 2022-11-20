import java.util.Arrays;

class arrays
{
    public static void main(String[] args)
    {
        // Arrays
        char vowels[] = {'a', 'e', 'i', 'o', 'u'};
        int numbers[] = {1, 10, 5, 9, 2};

        // Calling values in array
        System.out.println(vowels[0]);
        System.out.println(vowels[1]);
        System.out.println(vowels[4]);

        // Sorting arrays
        Arrays.sort(numbers);
        System.out.println(Arrays.toString(numbers));

        // Look for specific value in array (returns index of where the value is stored)
        // Only works on sorted arrays!
        int index = Arrays.binarySearch(numbers, 10);
        System.out.println(index);

        // Copy an array
        int copyNumbers[] = Arrays.copyOf(numbers, numbers.length);
        System.out.println(Arrays.toString(copyNumbers));

        // Copy array from certain index 
        int copyNumbersIndex[] = Arrays.copyOfRange(numbers, 1, 3);
        System.out.println(Arrays.toString(copyNumbersIndex));


    }
}