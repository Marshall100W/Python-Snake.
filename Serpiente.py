########## Abril 2024 ##########


from tkinter import *
import random
import time

ANCHO = 800
ALTO = 600
TAMAÑO_PPAL = str(ANCHO)+'x'+str(ALTO)

ANCHO_VERDE = 700
ALTO_VERDE = 450
TAMAÑO_BLOQUE = 20
VELOCIDAD = 120


direcc_x = 0
direcc_y = 0

def func_right(event):
    global direcc
    direcc = 1
    print('right')

def func_left(event):
    global direcc
    direcc = 2
    print('left')

def func_up(event):
    global direcc
    direcc = 3
    print('up')

def func_down(event):
    global direcc
    direcc = 4
    print('down')

def func_quit(event):
    print('FIN')
    quit()

def direccion():
    global direcc, direcc_x, direcc_y, tmp_direcc
    if time.time() > tmp_direcc:
        tmp_direcc = time.time()

        match direcc:
            case 1:
                if direcc_x == 0:
                    direcc_x = TAMAÑO_BLOQUE
                    direcc_y = 0
            case 2:
                if direcc_x == 0:
                    direcc_x = -TAMAÑO_BLOQUE
                    direcc_y = 0
            case 3:
                 if direcc_y == 0:
                    direcc_y = -TAMAÑO_BLOQUE
                    direcc_x = 0
            case 4:
                 if direcc_y == 0:
                    direcc_y = TAMAÑO_BLOQUE
                    direcc_x = 0

def colision():
    if head_x + direcc_x >= ANCHO_VERDE or head_x + direcc_x <= -20 or head_y + direcc_y >= ALTO_VERDE or head_y + direcc_y <= -20:
        label_fin = Label(ppal, text='GAME OVER!!!', bg='light green', fg='red', font=('Courier', 35))
        label_fin.place(x=230, y=220)
        ppal.update()
        ppal.bind('<Escape>', func_quit)


def mov_snake():
    global snake, head_x, head_y
    direccion()
    colision()

    for i in snake:
        ppal_canvas.create_rectangle(i[0],i[1],i[0]+TAMAÑO_BLOQUE, i[1]+TAMAÑO_BLOQUE, fill='green', outline='green')
    
    head_x += direcc_x
    head_y += direcc_y

    snake = snake[:-1]
    snake.insert(0, [head_x,head_y])
    for i in snake:
        ppal_canvas.create_rectangle(i[0],i[1],i[0]+TAMAÑO_BLOQUE, i[1]+TAMAÑO_BLOQUE, fill='light green')

    ppal.after(VELOCIDAD, mov_snake)


##########################################################################################################################################


ppal = Tk()
ppal.title('UP THE IRONS!')
ppal.geometry(TAMAÑO_PPAL)

ppal.bind('<Up>', func_up)
ppal.bind('<Down>', func_down)
ppal.bind('<Right>', func_right)
ppal.bind('<Left>', func_left)


ppal_canvas = Canvas(ppal, width=ANCHO_VERDE, height=ALTO_VERDE, background='green')
ppal_canvas.place(x=(int(ANCHO)-ANCHO_VERDE)/2, y=70)
head_x = random.randint(TAMAÑO_BLOQUE,int(ANCHO_VERDE/TAMAÑO_BLOQUE))*TAMAÑO_BLOQUE
head_y = random.randint(TAMAÑO_BLOQUE,int(ALTO_VERDE/TAMAÑO_BLOQUE))*TAMAÑO_BLOQUE
print(head_x, head_y)
direcc = 1
tmp_direcc = 0

snake = [[head_x,head_y], [head_x+TAMAÑO_BLOQUE*1,head_y], [head_x+TAMAÑO_BLOQUE*2,head_y],[head_x+TAMAÑO_BLOQUE*3,head_y], [head_x+TAMAÑO_BLOQUE*4,head_y]]

mov_snake()
ppal.mainloop()
