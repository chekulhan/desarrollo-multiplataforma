abstract class Person {
    String name;
    int age;

    // Constructor
    Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // Abstract method - tiene que estar implementado en sus subclasses - Student
    abstract void introduce();

    // Concrete method - compartido por todos los subclasses
    void sayHello() {
        System.out.println("Hello, my name is " + name);
    }
}

// Subclass of Person
class Student extends Person {
    String school;

    Student(String name, int age, String school) {
        super(name, age); // call Person constructor
        this.school = school;
    }

    // Implement abstract method
    @Override
    void introduce() {
        System.out.println("I am " + name + ", " + age + " years old, and I study at " + school);
    }

    // El Student puede override e implementar su propio sayHello() metodo
   

}


public class PersonApp {
    public static void main(String[] args) {
        //Person p = new Person("Alice", 30); // ❌ Not allowed, Person is abstract
        Student s = new Student("Alice", 20, "Greenwood High");

        s.sayHello();      // Calls concrete method from Person
        s.introduce();     // Calls implemented abstract method
    }
}