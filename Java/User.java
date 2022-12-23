public class User {

    // Set attributes as private
    private String name;
    private String membership;

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

    // Get membership method
    String get_membership() {
        return this.membership;
    }


}