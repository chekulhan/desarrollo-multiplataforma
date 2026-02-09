
# Encapsulación

La encapsulación es un principio fundamental de la programación orientada a objetos que consiste en proteger los datos de una clase evitando que sean accedidos o modificados directamente desde fuera de la clase. Esto se logra mediante:

- Atributos privados (private): Evitan que otras clases cambien directamente los valores internos.

- Métodos públicos (public): Permiten acceder o modificar los datos de manera controlada, aplicando reglas de negocio o validaciones.

La encapsulación ayuda a que el código sea más seguro, robusto y fácil de mantener, ya que cualquier cambio en los datos pasa por métodos controlados y predecibles.

Aqui tenemos un ejemplo de NO utilizar encapsulación:

Problema: cualquier código puede modificar balance de manera incorrecta, poniendo datos inválidos como balances negativos.
```java
class BankAcc {
  public int balance;
}


public class BankAccApp {
  public static void main(String[] args) {
    System.out.println("Hello world!");

    BankAcc b1 = new BankAcc();
    b1.balance = -50000;

    System.out.println("Balance: " + b1.balance);
  }
}
```

Ahora, tenemos un ejemplo con un buen uso de encapsulación en los atributos:

Ahora, con encapsulación, el código es seguro, robusto y confiable: los datos internos están protegidos y cualquier operación pasa por validaciones que evitan estados inválidos.

```java
class BankAcc {
  private int balance;

  public BankAcc(int balance) {
    this.balance = balance;
  }

  public void retirar(int amount)  {
    if (amount > 0 && amount <  this.balance) {
      this.balance -= amount;
    }
  }

  public int getBalance() {
    return this.balance;
  }
}


public class BankAccApp {
  public static void main(String[] args) {

    BankAcc b1 = new BankAcc(8);
    b1.retirar(5);
    System.out.println("Balance: " + b1.getBalance());
    b1.retirar(1);
    System.out.println("Balance: " + b1.getBalance());
    b1.retirar(10);
    System.out.println("Balance: " + b1.getBalance());

  }
}
```


## Actividad de Clase

Imagina que estás a cargo de la gestión del agua en un centro de datos, donde el agua se utiliza para la refrigeración de los servidores.

Tu tarea es diseñar una clase *DataCenter* que permita controlar el uso de agua de manera segura y controlada. La clase debe:

- Almacenar la cantidad de agua disponible (en litros) como un atributo privado.

- Permitir consumir agua, pero solo si hay suficiente disponible. Si no hay suficiente, debe mostrar un mensaje indicando que no se puede consumir esa cantidad.

- Permitir agregar agua al depósito, aumentando el total disponible.

- Proveer un método para consultar la cantidad actual de agua disponible.

En el programa principal (DataCenterApp) que instancia el objeto DataCenter con una cantidad inicial de agua.
Realiza varias operaciones de consumo y recarga de agua.
Muestra en pantalla la cantidad de agua después de cada operación.





---

### Respuesta:
class DataCenter {
    private int water; // liters of water available

    public DataCenter(int water) {
        this.water = water;
    }

    // Method that consumes water
    public void consumeWater(int amount) {
        if (amount > 0 && amount <= water) {
            water -= amount;
            System.out.println("Consumed " + amount + " liters of water.");
        } else {
            System.out.println("Not enough water to consume " + amount + " liters.");
        }
    }

    // Method to add water
    public void addWater(int amount) {
        if (amount > 0) {
            water += amount;
            System.out.println("Added " + amount + " liters of water.");
        }
    }

    // Getter
    public int getWater() {
        return water;
    }
}




public class DataCenterApp {
    public static void main(String[] args) {
        DataCenter dc = new DataCenter(1000); // start with 1000 liters

        dc.consumeWater(200);
        System.out.println("Water left: " + dc.getWater() + " liters");

        dc.consumeWater(900); // trying to consume more than available
        System.out.println("Water left: " + dc.getWater() + " liters");

        dc.addWater(500);
        System.out.println("Water after refill: " + dc.getWater() + " liters");
    }
}

