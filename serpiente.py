import turtle
import time
import random

# Configurar la ventana
window = turtle.Screen()
window.title("Serpiente")
window.bgcolor("black")
window.setup(width=600, height=600)
window.tracer(0)

# Cabeza de la serpiente
head = turtle.Turtle()
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Comida de la serpiente
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# Funciones de movimiento
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Configurar los controles de teclado
window.listen()
window.onkey(go_up, "w")
window.onkey(go_down, "s")
window.onkey(go_left, "a")
window.onkey(go_right, "d")

# Bucle principal del juego
while True:
    window.update()

    # Verificar colisiones con los bordes de la ventana
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Ocultar los segmentos de la serpiente
        for segment in segments:
            segment.goto(1000, 1000)

        # Limpiar la lista de segmentos
        segments.clear()

    # Verificar colisión con la comida
    if head.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)

        # Añadir un nuevo segmento a la serpiente
        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

    # Mover los segmentos de la serpiente en orden inverso
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Mover el primer segmento junto a la cabeza de la serpiente
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Verificar colisión de la cabeza con el cuerpo
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Ocultar los segmentos de la serpiente
            for segment in segments:
                segment.goto(1000, 1000)

            # Limpiar la lista de segmentos
            segments.clear()

    time.sleep(0.5)
