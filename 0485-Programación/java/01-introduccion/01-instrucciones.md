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