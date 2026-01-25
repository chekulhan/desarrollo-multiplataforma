// Dentro del mismo programa, no se usa 'public'
class Calculator {


    Calculator() {
        System.out.println("Calculator created");
    }

    public int add(int a, int b) {
        return a + b;
    }

    public int multiply(int a, int b) {
        return a * b;
    }
}

public class AppCalc2 {

    public static void main(String[] args) {

        Calculator calc = new Calculator();
        
        int sum = calc.add(5, 3);         
        int product = calc.multiply(5, 3); 

        System.out.println("Sum: " + sum);
        System.out.println("Product: " + product);
    }

}