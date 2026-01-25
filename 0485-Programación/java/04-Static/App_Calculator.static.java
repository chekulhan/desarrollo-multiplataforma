// Dentro del mismo programa, no se usa 'public'
class Calculator {

    // Static method → no object needed
    // Un método static es un método que pertenece a la clase, no a los objetos (instancias) de esa clase.
    // No necesitas crear un objeto para usarlo.

    public static int add(int a, int b) {
        return a + b;
    }

    public static int multiply(int a, int b) {
        return a * b;
    }
}

public class App_Calculator {
    public static void main(String[] args) {

        // No se ha instanciado la clase
        int sum = Calculator.add(5, 3);         
        int product = Calculator.multiply(5, 3); 

        System.out.println("Sum: " + sum);
        System.out.println("Product: " + product);
    }
}
