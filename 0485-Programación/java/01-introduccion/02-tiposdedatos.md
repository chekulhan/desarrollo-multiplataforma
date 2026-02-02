# Tipos de Datos

## Primitivos

| Type      | Example               | Size    | Notes            |
| --------- | --------------------- | ------- | ---------------- |
| `byte`    | `byte b = 100;`       | 1 byte  | Small integer    |
| `short`   | `short s = 1000;`     | 2 bytes | Small integer    |
| `int`     | `int i = 42;`         | 4 bytes | Standard integer |
| `long`    | `long l = 100000L;`   | 8 bytes | Large integer    |
| `float`   | `float f = 3.14f;`    | 4 bytes | Decimal number   |
| `double`  | `double d = 3.14159;` | 8 bytes | Decimal number   |
| `char`    | `char c = 'A';`       | 2 bytes | Single character |
| `boolean` | `boolean b = true;`   | 1 bit   | True or false    |

## Non-Primitivos

| Type       | Example                      | Notes                             |
| ---------- | ---------------------------- | --------------------------------- |
| `String`   | `String name = "Ana";`       | Sequence of characters            |
| Arrays     | `int[] nums = {1,2,3};`      | Collection of values              |
| Classes    | `Person p = new Person();`   | Objects with attributes & methods |
| Interfaces | `Runnable r = new Thread();` | Blueprint for classes             |


```java
int a = 5;
int b = 5;

if (a == b) {
    System.out.println("a and b are equal!");
}
```

```java
String name1 = "Jon";
String name2 = "Jon";
String name3 = new String("Jon");

System.out.println(name1 == name2);      // true — same literal in memory
System.out.println(name1 == name3);      // false — different objects
System.out.println(name1.equals(name3)); // true — content is the same
```
| Use case                              | What to use                                      |
|--------------------------------------|-------------------------------------------------|
| Primitives (`int`, `double`, `boolean`) | `==`                                           |
| Strings                               | `.equals()`                                     |
| Other objects (custom classes)        | `.equals()` (override for content equality if needed) |



# Actividad: “Informe del tiempo”

Objetivo: Practicar tipos de datos primitivos y no primitivos, arrays y salida por consola, creando un informe del tiempo para una semana con valores hard-coded (predefinidos).

Crear variables para:

- Nombre de la ciudad (String)
- Temperatura media (double)
- ¿Está lloviendo? (boolean)
- Día de la semana (usando char para la primera letra)
- Temperaturas diarias (int[] array)

Imprimir un resumen semanal del tiempo usando System.out.println.


---

## Respuesta

```java
public class WeatherReport {
    public static void main(String[] args) {

        // Non-primitive type
        String city = "Springfield";

        // Primitive types
        double avgTemp = 23.5;
        boolean isRaining = false;
        char dayOfWeek = 'M'; // Monday

        // Array of daily temperatures
        int[] dailyTemps = {22, 24, 21, 25, 23, 22, 24};

        // Print the weather report
        System.out.println("=== Weekly Weather Report ===");
        System.out.println("City: " + city);
        System.out.println("Average Temperature: " + avgTemp + "°C");
        System.out.println("Is it raining today? " + isRaining);
        System.out.println("First day of the week: " + dayOfWeek);

        System.out.print("Daily Temperatures: ");
        for (int temp : dailyTemps) {
            System.out.print(temp + "°C ");
        }
    }
}

```