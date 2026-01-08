# Instalacion
Son implementaciones de Open JDK (no hay diferencias en el código, sino en las licencias - Corretto is free para production)
- https://jdk.java.net/
- https://aws.amazon.com/es/corretto/

```bash
java -version
```

Java: Compile → Bytecode → JVM → JIT → Machine code
Python: Parse → Bytecode → Interpreter

Comandos para compilar y ejecutar:

```bash
javac HelloWorld.java       # compilar
java HelloWorld             # ejecutar

javap -c HelloWorld         # ver el bytecode
javap -c -verbose HelloWorld

# Bundle in a jar file:
jar cfe HelloWorld.jar HelloWorld HelloWorld.class

# c = create
# f = output file
# e = entry point (main class)


# y ejecutar con:
java -jar HelloWorld.jar

```

# Docker

Using openjdk:17-jdk-bullseye image as it has apt-get, so can install other required programs

Make sure in /java directory:

```bash
$ docker build -t java-dev .
```

Local directory is mounted to /workspace

```bash
$ docker run -it --name java-container \
    -v "$(pwd)":/workspace \
    -p 8080:8080 \
    java-dev
```


Create a new local file called HelloWorld.java:

```java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, Docker Java!");
    }
}
```

In Docker container:
Compile it: $ javac HelloWorld.java
Run it: $ java HelloWorld



# Historia de Java
Historia de Java
1995 – Nace Java (Sun Microsystems)


Java es propietario


Sun controla JDK, JVM y bibliotecas


Se populariza por “write once, run anywhere”


2006 – Nace OpenJDK


Sun libera OpenJDK bajo licencia GPL + Classpath Exception


Open-source, gratuito y comunidad puede contribuir


Sun sigue vendiendo su JDK comercial


2009 – Oracle compra Sun


Oracle se convierte en dueño de Java y OpenJDK


Oracle JDK = versión comercial con soporte pagado


OpenJDK = implementación oficial, gratuita y abierta


2010s – Consolidación


OpenJDK se convierte en referencia oficial de Java SE


Oracle JDK y OpenJDK prácticamente idénticos en funcionalidades


Surgen otras distribuciones basadas en OpenJDK:


Amazon Corretto


Eclipse Temurin


Azul Zulu


2020s – Java hoy


OpenJDK = núcleo gratuito y abierto


Oracle JDK = versión con soporte empresarial pagado


Otros JDK (Corretto, Temurin, Zulu) ofrecen LTS gratuitos


Java sigue siendo multiplataforma y ampliamente usado

