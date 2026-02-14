//https://repo1.maven.org/maven2/org/xerial/sqlite-jdbc/
// javac -cp ".;sqlite-jdbc-3.51.2.0.jar" DbApp.java
// java -cp ".;sqlite-jdbc-3.51.2.0.jar" DbApp   

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class DbApp {
    public static void main(String[] args) {
        // Path to your SQLite database file
        String url = "jdbc:sqlite:sample.db";

        // Try to establish a connection
        try (Connection conn = DriverManager.getConnection(url)) {
            if (conn != null) {
                System.out.println("Connection to SQLite has been established!");
            }
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }
    }
}
