import javax.swing.*;

// Simple Person class
class Person {
    private String name;
    private int age;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // Returns a readable string
    @Override
    public String toString() {
        return "Hola " + name + ", tienes " + age + " años";
    }
}

public class UIPersonaApp {
    public static void main(String[] args) {
        // Main form
        JFrame frame = new JFrame("Formulario Persona");
        frame.setSize(350, 250);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JPanel panel = new JPanel();
        panel.setLayout(null); // absolute positioning
        frame.add(panel);

        // Name label and field
        JLabel nameLabel = new JLabel("Nombre:");
        nameLabel.setBounds(10, 20, 80, 25);
        panel.add(nameLabel);

        JTextField nameField = new JTextField(20);
        nameField.setBounds(100, 20, 160, 25);
        panel.add(nameField);

        // Age label and field
        JLabel ageLabel = new JLabel("Edad:");
        ageLabel.setBounds(10, 60, 80, 25);
        panel.add(ageLabel);

        JTextField ageField = new JTextField(5);
        ageField.setBounds(100, 60, 50, 25);
        panel.add(ageField);

        // Label to show the Person info
        JLabel infoLabel = new JLabel("");
        infoLabel.setBounds(10, 140, 300, 25);
        panel.add(infoLabel);

        // Button to create the Person
        JButton createButton = new JButton("Crear Persona");
        createButton.setBounds(10, 100, 150, 25);
        panel.add(createButton);

        // Action on button click
        createButton.addActionListener(e -> {
            String nombre = nameField.getText();
            int edad = 0;

            edad = Integer.parseInt(ageField.getText());

            // Create Person and show info - do this in class
            //Person person = new Person(nombre, edad);
            //infoLabel.setText(person.toString());
        });

        frame.setVisible(true);
    }
}
