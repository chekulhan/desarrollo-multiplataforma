public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, Docker Java!");
    }
}




public class HelloWorld2 {

  public static void main(String[] args) {

    String name = "Jon  ";
    int age = 1;
    
    System.out.println("Hello " + name.toUpperCase().trim() + "X" );
    System.out.println("Goodbye "+ name.contains("on"));

    if (name.contains("on")) {
      System.out.println("Goodbye "+ name);
    }
    else {
      System.out.println("Hello "+ name);
    }


    for (int i=0; i< 10; i++) {
        System.out.println(i);
    }

    int i = 0;
    while (i < name.length()-1) {
      System.out.println(name.charAt(i)); // un String no es un array (lista) como en Python
      i ++;
    }


    // new switch
    switch (age) {
      case 1 -> System.out.println("You are 1"); 
      case 2 -> {
        int x = 55;
        System.out.println("You are " + x);
      }
      default -> System.out.println("You are not 1 or 2");
    }

    // classic switch - fijáte en el break!
    switch (age) {
        case 1: {
            System.out.println("You are 1");
            break;          // break is required to prevent fall-through
        }
        case 2: {
            System.out.println("You are 2");
            break;
        }
        default: {
            System.out.println("You are not 1 or 2");
        }
    }
    
  }

  
}