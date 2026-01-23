// Dentro del mismo programa, no se usa 'public'
class Calculator {

    // Static method → no object needed
    public static int add(int a, int b) {
        return a + b;
    }

    public static int multiply(int a, int b) {
        return a * b;
    }
}

public class App_Calculator {
    public static void main(String[] args) {
        int sum = Calculator.add(5, 3);         
        int product = Calculator.multiply(5, 3); 

        System.out.println("Sum: " + sum);
        System.out.println("Product: " + product);
    }
}
