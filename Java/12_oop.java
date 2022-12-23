class oop {
    public static void main(String[] args) {
        
        // Declaring object
        User user_1 = new User();

        // This set method cannot be used as attribute is set to private
        // user_1.name = "Ben";
        // user_1.membership = "Gold";

        // Using method getters & setters 
        user_1.set_name("Sally");
        user_1.set_membership(User.Membership.Gold);
        
        System.out.println(user_1.get_name());
        System.out.println(user_1.get_membership());
    }
}