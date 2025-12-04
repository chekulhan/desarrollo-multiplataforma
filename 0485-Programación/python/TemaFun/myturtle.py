import turtle

# Create a screen
screen = turtle.Screen()
screen.title("Basic Turtle Example")

# Create a turtle
t = turtle.Turtle()
t.shape("turtle")  # makes the cursor look like a turtle
t.color("blue")
t.speed(2)  # 1 = slow, 10 = fast

# Move the turtle
t.forward(100)  # move forward 100 units
t.left(90)      # turn 90 degrees left
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)

# Keep the window open until the user closes it
screen.mainloop()




# ACTIVIDAD : Convertir este ejemplo en funciones (function square())