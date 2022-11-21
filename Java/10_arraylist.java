import java.util.ArrayList;
import java.util.Comparator;

class arraylist {
    public static void main(String[] args) {

        // Creating an array list
        ArrayList<Integer> numbers = new ArrayList<Integer>();
        
        // Adding values in arraylist
        numbers.add(1);
        numbers.add(2);
        numbers.add(3);
        numbers.add(4);
        numbers.add(5);

        // Printing arraylist
        System.out.println(numbers.toString());

        // Printing value in specific index in arraylist
        System.out.println(numbers.get(0));

        // Removing value by index
        numbers.remove(0);

        // Removing value by value
        numbers.remove(Integer.valueOf(5));
        System.out.println(numbers.toString());

        // Update element in arraylist with index referencing
        numbers.set(1, 8);
        System.out.println(numbers.toString());

        // Sort arraylist
        // Must import java.util.Comparator
        numbers.sort(Comparator.naturalOrder());
        System.out.println(numbers.toString());

        numbers.sort(Comparator.reverseOrder());
        System.out.println(numbers.toString());

        // Check size of arraylist
        System.out.println("Array size: " + numbers.size());

        // Check if arraylist contains an element
        System.out.println(numbers.contains(Integer.valueOf(1)));

        // Clear entire arraylist
        numbers.clear();
        System.out.println("Final array: " + numbers.toString());

        // Check if arraylist is empty
        System.out.println(numbers.isEmpty());

        // Iterate within arraylist
        ArrayList<String> cars = new ArrayList<String>();
        
        cars.add("Volvo");
        cars.add("Ferrari");
        cars.add("Mercedes");

        cars.forEach(brand -> {
            System.out.print(brand +" ");
        });
    }
}