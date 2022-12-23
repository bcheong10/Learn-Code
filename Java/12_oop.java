import java.util.ArrayList;

class oop {
    public static void main(String[] args) {
        
        // Declaring object
        // User() is known as a constructor
        User user_1 = new User("Ben", "Gold");
        User user_2 = new User();

        // Creating a list of objects
        ArrayList<User> users = new ArrayList<User>();

        // Add users object into arraylist
        users.add(user_1);
        users.add(user_2);

        users.add(new User("Jon", "Silver"));

        // This set method cannot be used as attribute is set to private
        // user_1.name = "Ben";
        // user_1.membership = "Gold";

        // Using method getters & setters 
        user_2.set_name("Sally");
        user_2.set_membership(User.Membership.Bronze);
        
        System.out.printf("Name: %s, Membership: %s\n", user_1.get_name(), user_1.get_membership());
        System.out.printf("Name: %s, Membership: %s\n", user_2.get_name(), user_2.get_membership());
        System.out.println(user_1);

        // Print all users in arraylist
        for (User user: users) {
            System.out.println(user);
        }
    
    }
}