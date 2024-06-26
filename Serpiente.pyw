########## Abril 2024 ##########


from tkinter import *
import random
import time

ANCHO = 800
ALTO = 600
TAMAÑO_PPAL = str(ANCHO)+'x'+str(ALTO)

ANCHO_VERDE = 700
ALTO_VERDE = 460
TAMAÑO_BLOQUE = 20
FPS = 60

tmp_mov_snake = 0
vel_snake = 3
vel_snake_ = 0.5 / vel_snake
puntos = 0
fin = False

direcc_x = 0
direcc_y = 0
comida_x = -TAMAÑO_BLOQUE
comida_y = -TAMAÑO_BLOQUE

def inicio(event):
    global comida_x, comida_y, snake, head_x, head_y, fin, ppal_canvas, puntos, vel_snake, vel_snake_
    fin = False
    vel_snake = 3
    vel_snake_ = 0.5 / vel_snake
    ppal.unbind('<Escape>')
    ppal.unbind('<q>')
    puntos = -1
    score()
    ppal_canvas = Canvas(ppal, width=ANCHO_VERDE, height=ALTO_VERDE, background='green')
    ppal_canvas.place(x=(int(ANCHO)-ANCHO_VERDE)/2, y=70)

    head_x = random.randint(3,int((ANCHO_VERDE/TAMAÑO_BLOQUE))-3)*TAMAÑO_BLOQUE
    head_y = random.randint(3,int((ALTO_VERDE/TAMAÑO_BLOQUE))-3)*TAMAÑO_BLOQUE
    # comida_x = random.randint(3,int((ANCHO_VERDE/TAMAÑO_BLOQUE))-3)*TAMAÑO_BLOQUE
    # comida_y = random.randint(3,int((ALTO_VERDE/TAMAÑO_BLOQUE))-3)*TAMAÑO_BLOQUE

    snake = [[head_x,head_y], [head_x+TAMAÑO_BLOQUE*1,head_y], [head_x+TAMAÑO_BLOQUE*2,head_y],[head_x+TAMAÑO_BLOQUE*3,head_y], [head_x+TAMAÑO_BLOQUE*4,head_y]]

    comida()
    mov_snake()


def func_cursor(event):
    global direcc_x, direcc_y
    if event.keysym == 'Left':
        if direcc_x == 0:
            direcc_x = -TAMAÑO_BLOQUE
            direcc_y = 0

    if event.keysym == 'Right':
        if direcc_x == 0:
            direcc_x = TAMAÑO_BLOQUE
            direcc_y = 0

    if event.keysym == 'Up':
        if direcc_y == 0:
            direcc_y = -TAMAÑO_BLOQUE
            direcc_x = 0

    if event.keysym == 'Down':
        if direcc_y == 0:
            direcc_y = TAMAÑO_BLOQUE
            direcc_x = 0


def func_quit(event):
    print('FIN')
    ppal.destroy()


def score():
    global puntos
    puntos += 1
    label_puntos = Label(ppal, text='SCORE: {}  '.format(puntos), font=(35))
    label_puntos.place(x=500, y=30)
    print('Control')


def colision():
    global fin, vel_snake, vel_snake_
    if head_x + direcc_x >= ANCHO_VERDE + TAMAÑO_BLOQUE or head_x + direcc_x <= -TAMAÑO_BLOQUE*2 or head_y + direcc_y >= ALTO_VERDE + TAMAÑO_BLOQUE or head_y + direcc_y <= -TAMAÑO_BLOQUE*2:
        fin = True
        label_fin = Label(ppal, text='GAME OVER!!!', bg='light green', fg='red', font=('Courier', 35))
        label_fin.place(x=230, y=220)
        ppal.update()
        print('Colisión - X:', head_x, 'Y:', head_y)
        ppal.bind('<Escape>', func_quit)
        ppal.bind('<q>', inicio)


    if head_x + direcc_x == comida_x and head_y + direcc_y == comida_y:
        if vel_snake < 20:
            vel_snake += 0.5
            vel_snake_ = 0.5 / vel_snake
        score()
        comida()

def mov_snake():
    global tmp_mov_snake, snake, head_x, head_y

    if time.time() > tmp_mov_snake + vel_snake_:
        tmp_mov_snake = time.time()

        for i in snake:
            ppal_canvas.create_rectangle(i[0],i[1],i[0]+TAMAÑO_BLOQUE, i[1]+TAMAÑO_BLOQUE, fill='green', outline='green')
        
        head_x += direcc_x
        head_y += direcc_y
        snake = snake[:-1]
        snake.insert(0, [head_x,head_y])

        for i in snake:
            ppal_canvas.create_rectangle(i[0],i[1],i[0]+TAMAÑO_BLOQUE, i[1]+TAMAÑO_BLOQUE, fill='light green', outline='light green')

        colision()
    if not fin:
        ppal.after(FPS, mov_snake)


def comida():
    global comida_x, comida_y
    ppal_canvas.create_rectangle(comida_x, comida_y, comida_x + TAMAÑO_BLOQUE, comida_y + TAMAÑO_BLOQUE, fill='green', outline='green')
    comida_x = random.randint(3,int((ANCHO_VERDE/TAMAÑO_BLOQUE))-3)*TAMAÑO_BLOQUE
    comida_y = random.randint(3,int((ALTO_VERDE/TAMAÑO_BLOQUE))-3)*TAMAÑO_BLOQUE
    ppal_canvas.create_rectangle(comida_x, comida_y, comida_x + TAMAÑO_BLOQUE, comida_y + TAMAÑO_BLOQUE, fill='red', outline='green')
    print('Comida:', comida_x, '-', comida_y)


##########################################################################################################################################


ppal = Tk()
ppal.title('UP THE IRONS!')
ppal.geometry(TAMAÑO_PPAL)

ppal.bind('<Up>', func_cursor)
ppal.bind('<Down>', func_cursor)
ppal.bind('<Right>', func_cursor)
ppal.bind('<Left>', func_cursor)

inicio('x')

ppal.mainloop()


