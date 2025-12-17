# Teoría de la Carga Cognitiva (Cognitive Load Theory)

**Idea clave:**
Las personas tienen una capacidad limitada para procesar información al mismo tiempo. Si un informe muestra demasiados datos, el usuario se bloquea o lo ignora.

Aplicación en informes móviles
- Mostrar solo la información esencial
- Evitar pantallas llenas de números
- Usar resúmenes y luego permitir “ver más”

**El usuario entiende la situación en segundos, sin esfuerzo mental.**

# Teoría del Forrajeo de Información (Information Foraging Theory)
Los usuarios buscan información como si estuvieran “cazando”: quieren encontrar valor rápido y con poco esfuerzo.
Si no ven claramente qué les aporta un informe, abandonan.

Ejemplo: 
❌ Título: “Informe semanal”

✅ Título:“⚠️ Caída de ingresos esta semana”



# Principios Gestalt (Percepción Visual)

https://www.ilerna.es/blog/leyes-de-la-gestalt

Proximidad: Elementos cercanos se perciben como relacionados
Similitud: Elementos con el mismo color o forma significan lo mismo.
Jerarquía visual: El tamaño indica importancia. Texto grande = importante!


# Resumen:
Carga cognitiva: menos es más
Forrajeo de información: que se entienda en 5 segundos
Gestalt: el diseño también comunica, incluso sin texto


# Actividad en React Native
Agregamos al informe (componente) un Card de Pedidos, con un KPI de 56 y un trend positivo de ▲ 5% comparando con ayer.

Usar https://snack.expo.dev/

```jsx

import { Text, View, StyleSheet } from 'react-native';

export default function Informe() {
  return (
    <View style={styles.container}>
     <View style={styles.card}>
        <Text style={styles.kpiLabel}>Ventas hoy</Text>

        <Text style={styles.kpiValue}>
          €12.400
        </Text>

        <Text style={styles.trendNegative}>
          ▼ −8% vs ayer
        </Text>
      </View>



    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    alignItems: "center",
    justifyContent: "center",
    padding: 24,
    backgroundColor: "#f5f6f8",
  },

  spacer: {
    height: 16, // Gestalt: proximity (clear separation)
  },

  card: {
    backgroundColor: "#ffffff",
    padding: 16,
    borderRadius: 12,
    width: "100%",
    maxWidth: 320,
  },

  /* Gestalt: hierarchy */
  kpiLabel: {
    fontSize: 14,
    color: "#555",
    marginBottom: 6,
  },

  kpiValue: {
    fontSize: 28,
    fontWeight: "700",
    marginBottom: 8,
  },

  /* Information foraging */
  trendNegative: {
    fontSize: 13,
    fontWeight: "500",
    color: "#c62828",
  },

    
});

```
