import numpy as np
import tkinter as tk
import random

ancho = 28 
alto = 28   
tamano = 25  
dimension = 650
laberinto = [[1] * ancho for _ in range(alto)]  # Inicializa todo como muros

# Crear la ventana 
w = tk.Tk()
w.title("Laberinto")
canvas = tk.Canvas(w, width=dimension, height=dimension, bg="white")
canvas.pack()

# Matriz para el laberinto
laberinto = np.array([
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1],
])

direcciones = {
    "w": (0, -1),  # Ar
    "s": (0, 1),   # Ab
    "a": (-1, 0),  # I
    "d": (1, 0)    # D
}

# Posición inicial del jugador
jugador_x, jugador_y = 0, 0

# Función para generar el laberinto 
def generar_laberinto(x, y):
    laberinto[x][y] = 0  # Hacer el espacio visitado
    movimientos = list(direcciones.values())
    random.shuffle(movimientos)  # Aleatorizar las direcciones
    for dx, dy in movimientos:
        nx, ny = x + dx * 2, y + dy * 2
        if 0 <= nx < ancho and 0 <= ny < alto and laberinto[nx][ny] == 1:
            laberinto[x + dx][y + dy] = 0  # Abrir el camino
            generar_laberinto(nx, ny)

# Iniciar en la esquina superior izquierda
generar_laberinto(0, 0)

# Asegurarse de que la salida (27, 27) sea un camino
laberinto[alto - 1][ancho - 1] = 0  # Hacer la salida un camino
# Abrir celdas adyacentes a la salida
laberinto[alto - 2][ancho - 1] = 0  # Celda arriba
laberinto[alto - 1][ancho - 2] = 0  # Celda a la izquierda



def dibujar_laberinto():
    for i in range(ancho):
        for j in range(alto):
            x1 = i * tamano
            y1 = j * tamano
            x2 = x1 + tamano
            y2 = y1 + tamano
            if laberinto[i][j] == 1:
                canvas.create_rectangle(x1, y1, x2, y2, fill="black")  # Muros
            else:
                canvas.create_rectangle(x1, y1, x2, y2, fill="white")  # Caminos


def dibujar_entrada():
    x1 = 0 * tamano
    y1 = 0 * tamano
    x2 = x1 + tamano
    y2 = y1 + tamano
    canvas.create_rectangle(x1, y1, x2, y2, fill="red", outline="red")  # Entrada


def dibujar_salida():
    x1 = (ancho - 1) * tamano
    y1 = (alto - 1) * tamano
    x2 = x1 + tamano
    y2 = y1 + tamano
    canvas.create_rectangle(x1, y1, x2, y2, fill="red", outline="red")  # Salida


def dibujar_jugador(x, y):
    x1 = x * tamano
    y1 = y * tamano
    x2 = x1 + tamano
    y2 = y1 + tamano
    return canvas.create_rectangle(x1, y1, x2, y2, fill="blue", outline="blue", tags="jugador")


def mover_jugador(event):
    global jugador_x, jugador_y

    # dirección en función de la tecla presionada
    if event.char in direcciones:
        dx, dy = direcciones[event.char]
        nuevo_x, nuevo_y = jugador_x + dx, jugador_y + dy

        # posición es válida (no es un muro)
        if 0 <= nuevo_x < ancho and 0 <= nuevo_y < alto and laberinto[nuevo_x][nuevo_y] == 0:
            # Borrar la posición anterior 
            canvas.delete("jugador")
            
            # Actualiza la nueva posición 
            jugador_x, jugador_y = nuevo_x, nuevo_y
            
            # jugador en la nueva posición
            dibujar_jugador(jugador_x, jugador_y)


dibujar_laberinto()
dibujar_entrada()  
dibujar_salida()   

# jugador en la posición inicial
dibujar_jugador(jugador_x, jugador_y)

# teclaspara mover al jugador
w.bind("<KeyPress>", mover_jugador)


w.mainloop()