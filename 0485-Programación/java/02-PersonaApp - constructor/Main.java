public class Main {

    public static void main(String[] args) {
        Persona jon = new Persona("Jon", 21);
        Persona maria = new Persona("Maria", 78);


        System.out.println(jon);
        System.out.println(jon.getNombre());
        jon.setNombre("Johhny");
        System.out.println(jon.getNombre());


        System.out.println(maria);
    }
}
