
# Backlog refinement
El backlog refinement es la actividad en la que el equipo revisa y mejora el product backlog.

Se analizan las historias de usuario, se detallan requisitos, se corrigen ambigüedades, se estiman tamaños y se priorizan.

El objetivo es que las historias estén claras y listas para ser trabajadas en futuros sprints.


## Quiénes participan

- Product Owner (PO): guía las prioridades y clarifica los requisitos.

- Scrum Master: facilita la sesión y asegura que se cumpla el proceso.

- Equipo de desarrollo: aporta estimaciones, identifica dependencias y riesgos.

- A veces también participan stakeholders para aclarar dudas sobre necesidades del negocio.

## Frecuencia

Frecuencia recomendada: cada 1 o 2 semanas, para mantener el backlog actualizado y listo para los sprints.

## Actividad
- Usando la técnica de 't-shirt sizing', estimar la complejidad la complejidad usando t-shirts (S, M, L, XL). “relativo” = depende de la comparación con otras tareas, no de un valor absoluto fijo. Por ejemplo, 'S' comparando con 'L' es más complejo, pero no quiere decir 2 horas (absoluto).

- Usar MoSCoW para sacer 5 historias de usuarios para incluir en el siguiente sprint => priorizar

**MoSCoW**

Clasifica cada historia en cuatro categorías:

- M: Must have (Debe tener) → imprescindible

- S: Should have (Debería tener) → importante pero no crítica

- C: Could have (Podría tener) → opcional, nice-to-have

- W: Won’t have (No tendrá) → se pospone

# Historias de Usuarios

1. Como usuario, quiero poder filtrar productos por categoría, para encontrar más rápido lo que busco.

2. Como usuario, quiero recibir notificaciones cuando haya ofertas especiales, para no perderme descuentos.

3. Como usuario, quiero registrarme en la app usando mi correo electrónico y contraseña, para poder acceder a todas las funciones.

4. Como usuario, quiero iniciar sesión con mi cuenta de Google, para no tener que recordar otra contraseña.

5. Como usuario, quiero cambiar el tema de la app entre claro y oscuro, para personalizar la apariencia.

6. Como usuario, quiero poder ver un listado de productos en la pantalla principal, para decidir qué comprar.

7. Como usuario, quiero escribir reseñas sobre los productos que compré, para compartir mi opinión con otros usuarios.

8. Como usuario, quiero poder guardar mis productos favoritos en una lista de deseos, para comprarlos después.

9. Como usuario, quiero ver recomendaciones de productos basadas en mis compras anteriores, para descubrir cosas nuevas.

10. Como usuario, quiero recibir mensajes de ayuda dentro de la app con un chatbot, para resolver dudas rápidamente.

## Diversion con la programación en Javascript

```javascript
const historias = [
  "Como usuario, quiero poder filtrar productos por categoría, para encontrar más rápido lo que busco.",
  "Como usuario, quiero recibir notificaciones cuando haya ofertas especiales, para no perderme descuentos.",
  "Como usuario, quiero registrarme en la app usando mi correo electrónico y contraseña, para poder acceder a todas las funciones.",
  "Como usuario, quiero iniciar sesión con mi cuenta de Google, para no tener que recordar otra contraseña.",
  "Como usuario, quiero recibir mensajes de ayuda dentro de la app con un chatbot, para resolver dudas rápidamente."
];
```

Crear una función para:
- mostrar la lista de historias de usuarios al revés
- aleatoriamente - vaya reto!

Usar el algoritmo de Fisher y Yates:

https://www.youtube.com/watch?v=_rUa0cp6a1c


Cómo hacer un shuffle con Fisher-Yates, paso a paso:

1. Empezar desde el final del array

Comenzamos con el último elemento de la lista.

La idea es decidir aleatoriamente con quién se va a intercambiar.

2. Seleccionar un índice aleatorio

Para el elemento actual, elegimos un índice aleatorio entre 0 y la posición actual inclusive.

Este índice será el lugar con el que vamos a intercambiar el elemento.

```javascript
r = Math.floor(Math.random() * (i + 1)); // 0 ≤ r ≤ i
```

3. Intercambiar los elementos

Tomamos el elemento actual y lo intercambiamos con el elemento en el índice aleatorio seleccionado.

Esto garantiza que el elemento actual puede quedarse en su lugar o moverse a cualquier otra posición anterior.

4. Retroceder al elemento anterior

Bajamos una posición en la lista (hacia el principio) y repetimos el proceso:

Elegir un índice aleatorio entre 0 y la posición actual.

Intercambiar los elementos.

5. Repetir hasta el principio

Continuamos hasta llegar al primer elemento de la lista.

Al final, todos los elementos estarán mezclados aleatoriamente.