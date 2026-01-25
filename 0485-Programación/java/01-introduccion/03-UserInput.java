/*

En Python se usa input:

name = input("Enter your name: ")
print("Hello " + name)

*/

import java.util.Scanner;

public class UserInputBasic {

    public static void main(String[] args) {

      Scanner scanner = new Scanner(System.in);

      System.out.print("Enter your name: ");
      String name = scanner.nextLine(); // waits here until user presses Enter

      System.out.print("Enter your age: ");
      int age = scanner.nextInt();      // waits again for Enter

      System.out.println("Hello " + name + ", you are " + age + " years old.");
      scanner.close();
    }

}



/*

En Python se usa input con printf:

name = input("Enter your name: ")
print(f"Hello {name}")

*/

public class UserInputDataTypes {
    public static void main(String[] args) {

        // Different data types
        String name = "Ana";           // String
        int age = 20;                  // int
        double height = 1.65;          // double
        boolean isStudent = true;      // boolean
        char grade = 'A';              // char

        // Using String.format
        String message = String.format(
            "Name: %s\nAge: %d\nHeight: %.2f m\nStudent? %b\nGrade: %c",
            name, age, height, isStudent, grade
        );

        System.out.println(message);

        // Or using printf directly
        System.out.printf(
            "Name: %s\nAge: %d\nHeight: %.2f m\nStudent? %b\nGrade: %c\n",
            name, age, height, isStudent, grade
        );
    }
}
