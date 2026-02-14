import javax.swing.*;

public class GUI_Example1 {
    public static void main(String[] args) {
        // Primer formulario
        JFrame frame1 = new JFrame("Formulario 1");
        frame1.setSize(300, 200);
        frame1.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        JPanel panel1 = new JPanel();
        frame1.add(panel1);
        panel1.setLayout(null);

        // Label y TextField
        JLabel nameLabel = new JLabel("Nombre:");
        nameLabel.setBounds(10, 20, 80, 25);
        panel1.add(nameLabel);

        JTextField nameField = new JTextField(20);
        nameField.setBounds(100, 20, 160, 25);
        panel1.add(nameField);

        // Label y Input Box (JTextField también)
        JLabel ageLabel = new JLabel("Edad:");
        ageLabel.setBounds(10, 60, 80, 25);
        panel1.add(ageLabel);

        JTextField ageField = new JTextField(5);
        ageField.setBounds(100, 60, 50, 25);
        panel1.add(ageField);

        // Botón para abrir segundo formulario
        JButton openButton = new JButton("Abrir Formulario 2");
        openButton.setBounds(10, 100, 200, 25);
        panel1.add(openButton);


        JTextArea textArea = new JTextArea(5, 20);
        textArea.setBounds(200, 70, 50, 50);
        textArea.setEditable(true);
        panel1.add(textArea);

        openButton.addActionListener(e -> {
            // Mostrar los datos ingresados
            String nombre = nameField.getText();
            String edad = ageField.getText();
            showSecondForm(nombre, edad);
        });

        frame1.setVisible(true);
    }

    // Segundo formulario
    private static void showSecondForm(String nombre, String edad) {
        JFrame frame2 = new JFrame("Formulario 2");
        frame2.setSize(250, 150);
        JPanel panel2 = new JPanel();
        frame2.add(panel2);
        panel2.setLayout(null);

        JLabel infoLabel = new JLabel("Hola " + nombre + ", tienes " + edad + " años");
        infoLabel.setBounds(10, 20, 220, 25);
        panel2.add(infoLabel);

        frame2.setVisible(true);
    }
}
