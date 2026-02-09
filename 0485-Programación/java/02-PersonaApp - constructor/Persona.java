public class Persona {
   
    // Encapsulación
    private String nombre;
    private int edad;

    // Constructor
    public Persona(String nombre, int edad) {
        // conflictos con variables (ambiguidad), asi que usar this
        System.out.println("Persona constructor");
        this.nombre = nombre;
        this.edad = edad;
    }


    public String getNombre() {
        return this.nombre;
    }


    public void setNombre(String nombre) {
        this.nombre = nombre;
    }


}
