# Node
Antes de empezar con Electron, seria util reconocer un poco de  arrow functions y la programación asíncrona en Node.

## Arrow functions (ES6, 2015)

- Para hacer el código más limpio y corto.

- Para evitar problemas con this, especialmente en callbacks y métodos dentro de objetos.

- Para promover un estilo moderno de JavaScript (funciones como expresiones y programación funcional).

Función normal:

```js
function add (a, b) { 
    return a + b; 
};

const add = function(a, b) { 
    return a + b; 
};
```

```js
const add = (a, b) => a + b;
console.log(add(5, 3)); 


const add = (a, b) => {
  return a + b;
};

console.log(add(5, 3)); 


```

## Programación asíncrona

JavaScript es single-threaded (un solo hilo), lo que significa que solo puede ejecutar una cosa a la vez.

Para no bloquear el hilo principal, se introdujeron mecanismos asíncronos, que permiten ejecutar tareas “en segundo plano”.

Herramientas:
- setTimeout y setInterval (1996+)
- Callbacks (funciones de retorno) => muchos callbacks anidados surge el “callback hell”.
- Promises (ES6, 2015) => solucionan el callback hell
- async / await (ES8, 2017) => Permite escribir código asíncrono que parece síncrono, mucho más legible.

## Callback hell

```js
console.log("Inicio");

setTimeout(() => {
  console.log("Paso 1");

  setTimeout(() => {
    console.log("Paso 2");

    setTimeout(() => {
      console.log("Paso 3");

      setTimeout(() => {
        console.log("Paso 4 - Final");
      }, 1000);

    }, 1000);

  }, 1000);

}, 1000);
```

## setTimeout

```js
console.log("START");

setTimeout(()=> {
    console.log("Hello after a few secs")
}, 2000)

console.log("END");
```

setInterval
```js
let contador = 1;

const intervalo = setInterval(() => {
  console.log(contador);
  contador++;
  if (contador > 5) clearInterval(intervalo);
}, 1000);
```

## Actividades
### Actividad 1
Crear una funcion arrow para:
- multiplicar 2 números
- recibe un número y devuelve su cuadrado usando el operador **
- recibe dos números (base y exponente) y devuelve la base elevada al exponente.

### Actividad 2
Crear un programa para decir "Bienvenidos a la fiesta". 
Con un retraso, ya que vienen poco a poco a la fiesta, mostrar "Hola {nombre}":
- Mary, despues de 1 segundo
- Jon, despues de 2 segundos
- Susan, despues de 3 segundos

### Actividad 3
Usando setInterval y clearInterval, crear una function arrow para contar el lanzamiento de un cohete, desde 10, cada , hasta 0. Cuando llega a 0, iniciar un Blast Off!!!!

---
```js
const greet = (nombre) => {
    console.log(`Hola ${nombre}`);
}

console.log("Bienvenidos a la fiesta")
setTimeout(greet, 2000, 'Jon');
setTimeout(greet, 3000, 'Susan');
setTimeout(greet, 1000, 'Mary');


const delayedGreeting = (nombre, delay) => {
    setTimeout(() => {
        console.log(`Hola ${nombre}`);
    }, delay);
} 

console.log("Bienvenidos a la fiesta")
delayedGreeting('Jon', 2000);
delayedGreeting('Susan', 3000);
delayedGreeting('Mary', 1000);


let tiempo = 5;

const countdown = setInterval(()=> {
    if (tiempo>0) {
        console.log(`Counting ${tiempo}`);
        tiempo--;
    }
    else {
        console.log("Blast Off");
        clearInterval(countdown);
    }
}, 1000);
```