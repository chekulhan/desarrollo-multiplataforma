# Ejercicio: Convertidor de temperaturas

Crea una clase llamada ConvertidorTemperatura con dos métodos estáticos:

1. celsiusAFahrenheit(double celsius)

Debe convertir grados Celsius a Fahrenheit usando la fórmula:
```java
return celsius * 9 / 5 + 32;
```

2. fahrenheitACelsius(double fahrenheit)

Debe convertir grados Fahrenheit a Celsius usando la fórmula:
```java
return (fahrenheit - 32) * 5 / 9;
```

## Indicaciones:

- Los métodos deben ser static para poder llamarlos sin crear un objeto.

- En la clase Main, pide al usuario que ingrese una temperatura y usa los métodos para mostrar la conversión.

---









```java

class TemperatureConverter {

    // Convert Celsius to Fahrenheit
    static double celsiusToFahrenheit(double celsius) {
        return celsius * 9 / 5 + 32;
    }

    // Convert Fahrenheit to Celsius
    static double fahrenheitToCelsius(double fahrenheit) {
        return (fahrenheit - 32) * 5 / 9;
    }
}


public class Main {

    public static void main(String[] args) {

        double tempC = 25;
        double tempF = TemperatureConverter.celsiusToFahrenheit(tempC);
        System.out.println(tempC + "°C = " + tempF + "°F");

        double tempF2 = 77;
        double tempC2 = TemperatureConverter.fahrenheitToCelsius(tempF2);
        System.out.println(tempF2 + "°F = " + tempC2 + "°C");
    }
}

// Preguntar al usuario

import java.util.Scanner; // import Scanner class

public class Main {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in); // create a Scanner object

        System.out.print("Ingrese la temperatura en Celsius: ");
        double celsius = scanner.nextDouble(); // read a double value

        System.out.println("La temperatura ingresada es: " + celsius + "°C");

        scanner.close(); // close the scanner
    }
}



```


