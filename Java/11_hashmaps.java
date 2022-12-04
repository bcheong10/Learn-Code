import java.util.HashMap;

class hashmaps {
    public static void main(String[] args) {

        // HashMap<"Key", "value">
        HashMap<String, Integer> examScores = new HashMap<String, Integer>();

        // Put something into hashmap
        examScores.put("Math", 75);
        examScores.put("Sociology", 100);

        // Puts key value pair if it does not already exist in the hashmap
        // If it exists, it will not insert
        examScores.putIfAbsent("English", 90);

        // Prints hashmap
        System.out.println(examScores.toString());

        // Prints value of hashmap
        System.out.println(examScores.get("English"));

        // Replace key value pair
        examScores.replace("Math", 80);

        // Returns specific value if key does not exist
        System.out.println(examScores.getOrDefault("Religion", -1));
        
        // Removes key in hashmap
        examScores.remove("Math");

        // Checks if key exists
        System.out.println(examScores.containsKey("Math"));

        // Check if value exists
        System.out.println(examScores.containsValue(90));

        // Iterates through hashmap
        examScores.forEach((subject, score) -> {
            System.out.printf("%s: %d\n", subject, score);
        });

        // Clears hashmap
        examScores.clear();

        // .size() returns number of key value pairs in hashmap
        System.out.println(examScores.size());

        // Checks if hashmap is empty
        System.out.println(examScores.isEmpty());


    }
}