# Bucles

En Python, hariamos un bucle con una lista o tuple asi:

```python
daily_temps = [22, 24, 21, 25, 23, 22, 24]

for temp in daily_temps:
    print(f"{temp}°C ")
```

En Java:

```java
int[] dailyTemps = {22, 24, 21, 25, 23, 22, 24};

for (int temp : dailyTemps) {
    System.out.print(temp + "°C ");
}
```

En Python:

```python
# Print numbers from 1 to 5
for i in range(1, 6):
    print(i)
```

Y en Java:

```java
// Print numbers from 1 to 5
for (int i = 1; i <= 5; i++) {
    System.out.print(i + " ");
}
```


En Python:
```python
i = 1
while i <= 5:
    print(i)
    i += 1
```

Y en Java:
```java
int i = 1;
while (i <= 5) {
    System.out.print(i + " ");
    i++;
}

```