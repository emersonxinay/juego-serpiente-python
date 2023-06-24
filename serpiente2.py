# juego de la serpiente 
import turtle
import time
import random

# configurar la ventana 
window = turtle.Screen()
window.title("Juego de Serpiente")
window.bgcolor("blue")
window.setup(width=600, height=600)
window.tracer(0)

# cabeza de la serpiente 
cabeza = turtle.Turtle()
cabeza.shape("triangle")
cabeza.color("white")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction ="stop"

# la comida de la serpiente 
comida = turtle.Turtle()
comida.shape("circle")
comida.color("yellow")
comida.penup()
comida.goto(0, 100)

segmento = []

# funciones para los movimientos 
def go_up():
    if cabeza.direction != "down":
        cabeza.direction = "up"
        cabeza.setheading(90)

def go_down():
    if cabeza.direction != "up":
        cabeza.direction = "down"
        cabeza.setheading(-90)

def go_left():
    if cabeza.direction != "right":
        cabeza.direction = "left"
        cabeza.setheading(180)

def go_right():
    if cabeza.direction != "left":
        cabeza.direction = "right"
        cabeza.setheading(0)

def move():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y+20)
    
    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y-20)
    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x-20)
    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)

# configurar los controles de teclado 
window.listen()
window.onkey(go_up, "w")
window.onkey(go_down, "s")
window.onkey(go_left, "a")
window.onkey(go_right, "d")

# bucle principal del juego 
while True:
    window.update()
    # verificar las colisiones con los bordes de la ventana 
    if cabeza.xcor() > 290 or cabeza.xcor() < -290 or cabeza.ycor() > 290 or cabeza.ycor() < -290:
        time.sleep(1)
        cabeza.goto(0, 0)
        cabeza.direction = "stop"

        # ocultar los segmentos de la serpiente 
        for segment in segmento:
            segment.goto(1000, 1000)
        
        # limpiar la lista de los segmentos 
        segmento.clear()
    # verificar colisión con la comida 
    if cabeza.distance(comida) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        comida.goto(x, y)
        # añadir un nuevo segmento a la serpiente 
        new_segmento = turtle.Turtle()
        new_segmento.shape("circle")
        new_segmento.color("green")
        new_segmento.penup()
        segmento.append(new_segmento)
    # mover los segmentos de la serpiente 
    for index in range(len(segmento) -1, 0, -1 ):
        x = segmento[index - 1].xcor()
        y = segmento[index - 1].ycor()
        segmento[index].goto(x, y)

    # mover el segmento junto a la cabeza de la serpiente 
    if len(segmento) > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmento[0].goto(x, y)

    move()

    # verificar colision de la cabeza con el cuerpo 
    for segment in segmento:
        if segment.distance(cabeza) < 20:
            time.sleep(1)
            cabeza.goto(0,0)
            cabeza.direction = "stop"

            # ocultar los segmentos de la seripiente 
            for segment in segmento:
                segment.goto(1000, 1000)
            # limpiar la lista de segmentos 
            segmento.clear()
    time.sleep(0.5)






# para que no se cierre la ventana 
# turtle.done()