
# Sesion

Incluir  session, redirect, url_for from flask

Definimos un secret_key
```python
from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)

app.secret_key = "ABCD" 
```

Ahora, vamos a definir el proceso de login, dashboard y logout. Solo el dashboard estará disponible si el usuario 'bob' ha hecho el login.

```python
@app.route("/login")
def login():
    session["username"] = "bob"
    return f"Logged In {session.get('username')}"

@app.route("/dashboard")
def dashboard():
    print(session)
    username = session.get("username")
    if username:
        return f"Dashboard for user {username}"
    else:
        return redirect(url_for("login")) # protect route
        
@app.route("/logout")
def logout():
    session.pop("username", None)
    return "Logged Out"
```