
Incluimos render_template

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/welcome1")
def welcome1():
    nombre = "Jon"
    return render_template("welcome.html", nombre=nombre)

@app.route("/welcome2")
def welcome2():

    user_info = {
        "nombre": "Alice",
        "edad": 30,
    }
    return render_template("welcome.html", user=user_info)

if __name__ == "__main__":
    app.run(debug=True)

```

```html
<body>
    <h1>Hello {{nombre}}</h1>
    <h2>Hello {{user.nombre}}</h2>
    <h2>Hello {{user.edad}}</h2>
</body>

```

```python

def users():
    users = [
        {"nombre": "alice", "edad": 30},
        {"nombre": "bob", "edad": 25}
    ]
    return render_template("users.html", users = users)
```

```html
<h1>All Users</h1>
<ul>
{% for user in users %}
    <li>{{ user.nombre }} - Edad: {{ user.edad }}</li>
{% endfor %}
</ul>

```


## Actividad

Trabajas en un centro de salud, donde hay que mostrar datos sobre las calorias, azúcares y cantidad de agua bebida (mostrar estos datos al priipio de la pagina web). 
Despues, en la misma página:
- mostrar una lista de comida basura: junk_foods = ["Chocolate Bar", "Potato Chips", "Soda", "Ice Cream", "Candy"], usando un  <ul><li> 
- mostrar los mismos datos en un <select> de html

Ojo, se puede pasar más de un dato desde el servidor web a la página, como ves con las variables de a y b:

```python
return render_template('index.html', a=a,b=b)
```