class strings
{
    public static void main(String[] args)
    {
        // Takes up the same memory location
        String literalString1 = "abc";
        String literalString2 = "abc";

        // Object string using the "new" keyword has different memory location and are not the same
        String objectString1 = new String("xyz");
        String objectString2 = new String("xyz");

        // Prove:
        System.out.println(literalString1 == literalString2);
        System.out.println(objectString1 == objectString2);

        // Formatted string
        String name = "Ben"; // %s
        int age = 23; // %d
        double gpa = 3.75; // %f

        String formatted = String.format("My name is %s, I am %d years old", name, age);
        System.out.println(formatted);

        // Find the length of a string
        System.out.println(name.length());

        // Find if String variable is empty
        System.out.println(name.isEmpty());

        // Covert to lowercase/uppercase
        System.out.println(name.toUpperCase());
        System.out.println(name.toLowerCase());

        // Replace strings
        String statement = "Hello, my name is Ben";
        System.out.println(statement.replace("Ben", "Amy"));

        // Checks if String contains a certain word
        System.out.println(statement.contains("Hello"));
    }
}