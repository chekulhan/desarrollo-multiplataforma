
# Herencia y Polimor
Herencia en Java es el mecanismo por el cual una clase (subclase) puede heredar atributos y métodos de otra clase (superclase). Permite reutilizar código, organizar mejor la estructura del programa y establecer relaciones del tipo “es-un” (por ejemplo, una subclase es un tipo de la superclase).

El polimorfismo con métodos permite que un mismo método pueda comportarse de manera diferente según el objeto que lo ejecute. Esto ocurre principalmente mediante la sobrescritura de métodos (method overriding), donde una subclase redefine un método heredado para adaptarlo a su propio comportamiento.

Gracias al polimorfismo, se puede trabajar con referencias del tipo de la superclase y ejecutar dinámicamente el método correspondiente a la subclase en tiempo de ejecución (enlace dinámico o dynamic binding).

```java
class Animal {

    public boolean estaVivo;

    public Animal(boolean estaVivo) {
        this.estaVivo = estaVivo;
    }

    public String hablar() {
        return "Animal hablando...";
    }
}


class Perro extends Animal {

    public int patas;

    public Perro(boolean estaVivo, int patas) {
        super(estaVivo);
        this.patas = 4;
    }


    public String hablar() {
        return "Woof woof";
    }
}


public class AnimalApp { 

    public static void main(String[] args) { 

        Perro animal = new Perro(true, 4);
        System.out.println("Animal " + animal.estaVivo);
        System.out.println(animal.hablar());
        System.out.println(animal.patas);

        // Terminar con el Gato

    }
}

```

**@Override** es una anotación que indica que un método en una subclase está destinado a sobrescribir (redefinir) un método **heredado de la superclase**.

- Se coloca encima del método.
- No es obligatorio, pero es una buena práctica.


```java
import java.util.ArrayList;

class Animal {

    public boolean estaVivo;

    public Animal(boolean estaVivo) {
        this.estaVivo = estaVivo;
    }

    public String hablar() {
        return "Animal hablando...";
    }
}

class Perro extends Animal {

    public Perro(boolean estaVivo) {
        super(estaVivo);
    }

    @Override
    public String hablar() {
        return "Woof woof";
    }
}

public class AnimalApp {

    public static void main(String[] args) {

        ArrayList<Animal> animales = new ArrayList<>();

        animales.add(new Perro(true));
        animales.add(new Perro(false));

        for (Animal a : animales) {
            System.out.println(a.hablar());
        }
    }
}
```

## Actividad

Tocas en un grupo de música. Hay una guitarista, un bajo y piano. 

¿Pensar como seria la herencia? 

Al final, agregar todos los instrumentos a una ArrayList<Instrumentos> para que puedan tocar todos...



### Respuesta
```java
import java.util.ArrayList;

class Instrumento {

    public String nombre;
    public String marca; // nueva propiedad

    public Instrumento(String nombre, String marca) {
        this.nombre = nombre;
        this.marca = marca;
    }

    public String tocar() {
        return "Instrumento sonando...";
    }
}

class GuitarraElectrica extends Instrumento {

    public GuitarraElectrica(String marca) {
        super("Guitarra Eléctrica", marca);
    }

    @Override
    public String tocar() {
        return "Tocando riffs de guitarra eléctrica";
    }
}

class Bajo extends Instrumento {

    public Bajo(String marca) {
        super("Bajo", marca);
    }

    @Override
    public String tocar() {
        return "Tocando líneas de bajo";
    }
}

class Piano extends Instrumento {

    public Piano(String marca) {
        super("Piano", marca);
    }

    @Override
    public String tocar() {
        return "Tocando melodías en el piano.";
    }
}

public class BandaApp {

    public static void main(String[] args) {

        ArrayList<Instrumento> banda = new ArrayList<>();

        banda.add(new GuitarraElectrica("Fender"));
        banda.add(new Bajo("Ibanez"));
        banda.add(new Piano("Yamaha"));

        for (Instrumento i : banda) {
            System.out.println(i.marca + " " + i.nombre + ": " + i.tocar());
        }
    }
}
```
