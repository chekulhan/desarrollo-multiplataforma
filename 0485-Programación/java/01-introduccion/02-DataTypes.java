public class DataTypes {
    public static void main(String[] args) {

        // Primitive types
        int age = 20;
        double height = 1.75;
        boolean isStudent = true;
        char grade = 'A';

        // Non-primitive types
        String name = "Ana";
        int[] scores = {90, 85, 78};

        // Display primitive types
        System.out.println("=== Primitive Types ===");
        System.out.println("Age: " + age);
        System.out.println("Height: " + height);
        System.out.println("Is student? " + isStudent);
        System.out.println("Grade: " + grade);

        // Display non-primitive types
        System.out.println("\n=== Non-Primitive Types ===");
        System.out.println("Name: " + name);
        System.out.print("Scores: ");
        for (int score : scores) {
            System.out.print(score + " ");
        }
    }
}
