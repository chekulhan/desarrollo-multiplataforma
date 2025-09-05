# JSDoc
## 📘 ¿Qué es JSDoc?
JSDoc es una herramienta y una convención de comentarios que permite documentar el código JavaScript directamente dentro del propio archivo fuente. Sirve para que:

- Tú y otros desarrolladores entiendan mejor el código.

- Se generen automáticamente documentos HTML legibles.

- Se obtenga autocompletado y ayuda contextual en editores como VSCode.

https://jsdoc.app/

## Ejemplos

```js
/**
 * Calcula el área de un rectángulo.
 * 
 * @param {number} ancho - El ancho del rectángulo.
 * @param {number} alto - El alto del rectángulo.
 * @returns {number} El área calculada.
 */
function calcularArea(ancho, alto) {
  return ancho * alto;
}

```

```jsx
import React from 'react';

/**
 * Componente para mostrar un saludo personalizado.
 * @component
 * @example
 * // Ejemplo de uso
 * <Greeting name="Juan" />
 * 
 * @param {Object} props - Las propiedades del componente.
 * @param {string} props.name - El nombre de la persona a saludar.
 * @returns {JSX.Element} El saludo renderizado.
 */
const Greeting = ({ name }) => {
  return (
    <div>
      <h1>¡Hola, {name}!</h1>
    </div>
  );
};

export default Greeting;

```

Al usarlo, aparecerá la información de la función:

![Ejemplo de uso](../../x-assets/UF1844/jsdoc.png)

## Instalacion
Vamos a instalar JSDoc en nuestro aplicacion de Node (usar un **sub-directorio** de la aplicacion MERN)

```bash
npm init -y
```
Agregar `"type": "module",` al archivo package.json.


```bash
npm install --save-dev jsdoc
```

Creamos un archivo de matemáticas (mathFunctions.js):

```js
/**
 * Suma dos números.
 * @param {number} a - El primer número a sumar.
 * @param {number} b - El segundo número a sumar.
 * @returns {number} El resultado de la suma de a y b.
 */
export function sumar(a, b) {
    return a + b;
  }
  
  /**
   * Divide dos números.
   * @param {number} a - El numerador.
   * @param {number} b - El denominador.
   * @returns {number} El resultado de la división de a entre b.
   * @throws {Error} Lanza un error si el denominador es cero.
   */
export function dividir(a, b) {
    if (b === 0) {
      throw new Error('No se puede dividir entre cero');
    }
    return a / b;
  }
  
```

Generar la documentación:

```bash
npx jsdoc mathfunctions.js
```

Se puede añadir más archivos x.js, y.js o *.js


## Actividades


1. Generar JSDocs para:
```js
export function almacenarEnLocalStorage(clave, valor) {
    localStorage.setItem(clave, JSON.stringify(valor));
  }
  ```

2. ¿Qué resultado consigues con este clase?

```js
/**
 * Clase que realiza cálculos financieros.
 * @class
 */
class FinancialCalculator {
  /**
   * Crea una instancia del calculador financiero.
   * @constructor
   * @param {number} principal - El monto principal (la cantidad de dinero inicial).
   */
  constructor(principal) {
    /**
     * El monto inicial de dinero.
     * @type {number}
     */
    this.principal = principal;
  }

  /**
   * Calcula el interés compuesto.
   * 
   * La fórmula del interés compuesto es:
   * A = P (1 + r/n)^(nt)
   * Donde:
   *   - A es el monto acumulado después de n años, incluyendo el interés.
   *   - P es el monto principal (la cantidad de dinero inicial).
   *   - r es la tasa de interés anual (en forma decimal).
   *   - n es el número de veces que se compone el interés al año.
   *   - t es el tiempo en años.
   *
   * @param {number} rate - La tasa de interés anual (r) en formato decimal (por ejemplo, 0.05 para 5%).
   * @param {number} timesCompounded - El número de veces que se compone el interés al año (n).
   * @param {number} time - El tiempo en años (t).
   * @returns {number} - El monto acumulado (A) después del interés compuesto.
   * 
   * @example
   * const calc = new FinancialCalculator(1000);
   * const result = calc.calculateCompoundInterest(0.05, 4, 5);
   * console.log(result); // 1283.68
   */
  calculateCompoundInterest(rate, timesCompounded, time) {
    const amount = this.principal * Math.pow(1 + rate / timesCompounded, timesCompounded * time);
    return amount.toFixed(2); // Devuelve el monto acumulado, redondeado a 2 decimales
  }

  /**
   * Calcula el pago mensual de un préstamo utilizando la fórmula de amortización.
   * 
   * La fórmula del pago del préstamo es:
   * M = P [ r(1 + r)^n ] / [ (1 + r)^n - 1]
   * Donde:
   *   - M es el pago mensual total.
   *   - P es el monto del préstamo (principal).
   *   - r es la tasa de interés mensual (tasa anual dividida por 12).
   *   - n es el número de pagos (término del préstamo en meses).
   *
   * @param {number} annualRate - La tasa de interés anual (r) en formato decimal (por ejemplo, 0.05 para 5%).
   * @param {number} months - El número total de pagos (n), es decir, el término del préstamo en meses.
   * @returns {number} - El pago mensual (M).
   * 
   * @example
   * const calc = new FinancialCalculator(10000);
   * const monthlyPayment = calc.calculateLoanPayment(0.05, 60);
   * console.log(monthlyPayment); // 188.71
   */
  calculateLoanPayment(annualRate, months) {
    const monthlyRate = annualRate / 12;
    const payment = this.principal * (monthlyRate * Math.pow(1 + monthlyRate, months)) / (Math.pow(1 + monthlyRate, months) - 1);
    return payment.toFixed(2); // Devuelve el pago mensual, redondeado a 2 decimales
  }
}

// Ejemplo de uso

const calculator = new FinancialCalculator(1000);

// Cálculo de interés compuesto
const compoundInterest = calculator.calculateCompoundInterest(0.05, 4, 5);
console.log(`Interés compuesto: $${compoundInterest}`);

// Cálculo de pago mensual de préstamo
const loanPayment = calculator.calculateLoanPayment(0.05, 60);
console.log(`Pago mensual del préstamo: $${loanPayment}`);


```



## Respuestas

/**
 * Almacena un valor en el LocalStorage.
 * @param {string} clave - La clave con la que se almacenará el valor.
 * @param {any} valor - El valor a almacenar, que será convertido a una cadena.
 */
export function almacenarEnLocalStorage(clave, valor) {
    localStorage.setItem(clave, JSON.stringify(valor));
  }

Recordar que hay que export las funciones, y incluirlos como import:
```jsx
import {FinancialCalculator} from './finance.js';
```