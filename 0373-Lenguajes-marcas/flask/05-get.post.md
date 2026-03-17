

```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/submit", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        edad = request.form.get("edad")

        # Pass variables to Jinja template
        return render_template("result.html", nombre=nombre, edad=edad)

    return render_template("form.html")

```


```html
<!DOCTYPE html>
<html>
<body>
  <h2>Introducir tus datos</h2>

  <form method="POST" action="/submit">
    <input type="text" name="nombre" placeholder="Nombre">
    <input type="number" name="edad" placeholder="Edad">
    <button type="submit">Submit</button>
  </form>

</body>
</html>
```