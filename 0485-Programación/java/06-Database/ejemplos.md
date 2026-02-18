# JDBC - Base de datos sqlite con Java

Java no sabe hablar directamente con una base de datos. Necesita un traductor. Ese traductor es el **driver**.


**JDBC = Java Database Connectivity**
Es una API estándar de Java para conectarse a bases de datos.

Lo importante:
- JDBC define interfaces
- El driver implementa esas interfaces
- Cada base de datos tiene su propio driver

## SQLite
Ese archivo es la biblioteca JDBC para SQLite. Debes colocarlo en la misma carpeta donde estará tu código Java (o en un directorio desde donde lo referenciarás).

https://repo1.maven.org/maven2/org/xerial/sqlite-jdbc/

Ese .jar contiene:

- Clases que implementan java.sql.Driver
- Código que traduce llamadas JDBC a instrucciones que entiende SQLite
- En el caso de SQLite, incluso incluye el motor nativo embebido

## Compilar el programa Java

-cp Classpath: donde Java busca clases y librerías

Java no sabría qué es SQLite si no le dices dónde está la biblioteca.

```bash
javac -cp ".;sqlite-jdbc-3.51.2.0.jar" DbApp.java
```

En Windows se usa punto y coma ; para separar rutas.
En Linux/macOS se usa dos puntos : en vez de ;.


## Ejecutar el programa

```bash
java -cp ".;sqlite-jdbc-3.51.2.0.jar" DbApp  
```

En Windows se usa punto y coma ; para separar rutas.
En Linux/macOS se usa dos puntos : en vez de ;.

```bash
javac -cp ".:sqlite-jdbc-3.51.2.0.jar" DbApp.java
java -cp ".:sqlite-jdbc-3.51.2.0.jar" DbApp
```

## Ejemplos de código

En este ejemplo, estamos creando una tabla clientes si no existe, e insertando datos (dos records de clientes)

```java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;

public class DbApp {

    public static void main(String[] args) throws Exception {

        String url = "jdbc:sqlite:sample.db";

        // SQL to create the clients table
        String createTableSql = "CREATE TABLE IF NOT EXISTS clients (" +
                                "id INTEGER PRIMARY KEY," +
                                "name TEXT NOT NULL," +
                                "email TEXT" +
                                ");";

        // SQL to insert some sample clients
        String insertSql1 = "INSERT INTO clients (name, email) VALUES ('Alice', 'alice@example.com');";
        String insertSql2 = "INSERT INTO clients (name, email) VALUES ('Bob', 'bob@example.com');";

        Connection conn = DriverManager.getConnection(url);
        Statement stmt = conn.createStatement();

        // Create table
        stmt.execute(createTableSql);
        System.out.println("Table 'clients' created (if it did not exist).");

        // Insert sample data
        stmt.executeUpdate(insertSql1);
        stmt.executeUpdate(insertSql2);
        System.out.println("Inserted 2 sample clients.");

        stmt.close();
        conn.close();
    }
}

```

En este ejemplo, estamos mostrando los datos de la tabla clientes, a través de un ResultSet
El ResultSet contiene un conjunto de resultados, en la memoria, TYPE_FORWARD_ONLY (solo puedes ir para adelante, no atrás) and CONCUR_READ_ONLY (no se puede modificar los datos).

```java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

public class DbApp {

    public static void main(String[] args) throws Exception {

        String url = "jdbc:sqlite:sample.db";
        String sql = "SELECT id, name, email FROM clients";

        Connection conn = DriverManager.getConnection(url);
        Statement stmt = conn.createStatement();
        ResultSet rs = stmt.executeQuery(sql);  // FOWARD only, READ only resultset

        while (rs.next()) { 
            System.out.println(
                rs.getInt("id") + " | " +
                rs.getString("name") + " | " +
                rs.getString("email")
            );
        }

        rs.close();
        stmt.close();
        conn.close();
    }
}
```

En este ejemplo, estamos usando prepareStatement para insertar y actualizar datos:

```java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;

public class DbApp {

    public static void main(String[] args) throws Exception {

        String url = "jdbc:sqlite:sample.db";

        Connection conn = DriverManager.getConnection(url);

        // INSERT
        String insertSql = "INSERT INTO clients(name, email) VALUES(?, ?)";

        PreparedStatement insertStmt = conn.prepareStatement(insertSql);
        insertStmt.setString(1, "Ana Lopez");
        insertStmt.setString(2, "ana@email.com");

        int rowsInserted = insertStmt.executeUpdate();
        System.out.println("Filas insertadas: " + rowsInserted);

        insertStmt.close();


        // UPDATE
        String updateSql = "UPDATE clients SET email = ? WHERE name = ?";

        PreparedStatement updateStmt = conn.prepareStatement(updateSql);
        updateStmt.setString(1, "ana.nuevo@email.com");
        updateStmt.setString(2, "Ana Lopez");

        int rowsUpdated = updateStmt.executeUpdate();
        System.out.println("Filas actualizadas: " + rowsUpdated);

        updateStmt.close();

        conn.close();
    }
}

```

Este ejemplo **NO** es para production y es solo para ayudar entender los conceptos y poner en la práctica el acceso a una base de datos desde un objeto. Realmente lo hariamos con una clase de DAO (Data Access Object) o ORM (Object Relational Mapping).

```java
public class Client {

 ...

  
    public void save() throws Exception {

        String url = "jdbc:sqlite:sample.db";
        String sql = "INSERT INTO clients(name, email) VALUES(?, ?)";

        Connection conn = DriverManager.getConnection(url);

        PreparedStatement stmt = conn.prepareStatement(sql);
        stmt.setString(1, this.name);
        stmt.setString(2, this.email);

        stmt.executeUpdate();

        stmt.close();
        conn.close();
    }

    ...
}
```