from random import *
from turtle import *
from freegames import path
import string

car = path('car.gif')
alphabet = list(string.ascii_uppercase)
lower_letters = ['a','b','c','d','e','f']
tiles = alphabet + lower_letters + alphabet + lower_letters
state = {'mark': None}
hide = [True] * 64
taps = 0 # contador
complete = False # Juego completado
cont_complete = 0 #Contador para completado

def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    
    global taps
    spot = index(x, y)
    mark = state['mark']

    if hide[spot]:
        taps += 1
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None


def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()
    #mostrar contador en el juego
    up()
    goto(0, 220)
    color('black')
    write(f'TAPS: {taps}', align='center', font=('Comic Sans', 24, 'bold'))


    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)


    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 25, y )
        color('black')
        # para centrar los numeros en el memorama
        write(tiles[mark], align ="center", font=('Arial', 30, 'normal'))
    for casilla in hide:
        if(casilla) == False:
            global cont_complete
            cont_complete += 1
    if (cont_complete == 64):
        up()
        goto(-40,-300)
        down()
        color('black')
        write("Rompecabezas completado",font=('Comic Sans',24,'bold'))
    cont_complete = 0
    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
