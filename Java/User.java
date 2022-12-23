import java.text.Format;

public class User {

    // Set attributes as private
    private String name;
    private String membership;

    // Creating a Constructor
    public User(String name, String membership) {
        this.name = name;
        this.membership = membership;

        // Or we can invoke the getter and setter methods:
        // set_name(name)
        // set_membership(membership)
    }

    // Creating a default constructor to enable default calling of object
    public User() {

    }
    
    // Method overriding 
    // Returns this function when printing the object variable
    public String toString() {
        return "Name: " + this.name + "\n" + "Membership: " + this.membership;
    }

    // ---------------------------------------- METHODS -------------------------------------------------------------
    // Method #1 (or Functions in python) (Setters)
    void set_name(String name) {
        this.name = name;
    }

    // Method #2 (Getters)
    String get_name() {
        return this.name;
    }

    // Creating enums
    public enum Membership {
        // Constants
        Bronze, Silver, Gold;
    }

    // Set membership method
    void set_membership(Membership membership) {
        // .name() returns the name of the enums constants
        this.membership = membership.name();
    }

    // Set membership method (String)
    void set_membership(String membership) {
        this.membership = membership;
    }

    // Get membership method
    String get_membership() {
        return this.membership;
    }


}