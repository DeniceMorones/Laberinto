import numpy as np
import tkinter as tk
from tkinter import simpledialog, messagebox

# Configuración del laberinto
ancho = 28
alto = 21  # Cambia el valor de 28 a 21

tamano = 25
dimension = 700

# Crear ventana y canvas para el laberinto
w = tk.Tk()
w.title("Laberinto Dinámico")
canvas = tk.Canvas(w, width=dimension, height=dimension, bg="white")
canvas.pack()

# Laberinto: 0 = camino, 1 = muro, 2 = salida, 3 = teletransporte, 4 = destino teletransporte, 111 = trivia
laberinto = np.array([
    [0, 0, 0, 1, 0, 0, 3, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 2, 1],
    [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 4, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 111, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
])

# Diccionario de direcciones
direcciones = {
    "w": (0, -1),  # arriba
    "s": (0, 1),   # abajo
    "a": (-1, 0),  # izquierda
    "d": (1, 0)    # derecha
}

# Teletransportadores
teletransportadores = {
    (6, 0): (6, 6),
    (6, 6): (6, 0)
}

# Posición inicial
jugador_x = 0
jugador_y = 0

# mover
def mover_teletransportador(x, y):
    if (x, y) in teletransportadores:
        return teletransportadores[(x, y)]
    return (x, y)

def resolver_acertijo():
    respuesta = simpledialog.askstring("Acertijo", "¿Cuál es la capital de Francia?")
    return respuesta.lower() == "París"

def mover_con_acertijo(x, y):
    if laberinto[y][x] == 111:
        if resolver_acertijo():
            laberinto[y][x] = 0  # Si se resuelve, se convierte en camino
        else:
            messagebox.showwarning("Acertijo incorrecto", "Respuesta incorrecta. No puedes pasar.")
            return False
    return True

def mover_jugador(event):
    global jugador_x, jugador_y

    if event.char in direcciones:
        dx, dy = direcciones[event.char]
        nuevo_x, nuevo_y = jugador_x + dx, jugador_y + dy

        #teletransportador si aplica
        nuevo_x, nuevo_y = mover_teletransportador(nuevo_x, nuevo_y)

        #verificar acertijos
        if mover_con_acertijo(nuevo_x, nuevo_y):
            if 0 <= nuevo_x < ancho and 0 <= nuevo_y < alto and laberinto[nuevo_y][nuevo_x] != 1:
                canvas.delete("jugador")
                jugador_x, jugador_y = nuevo_x, nuevo_y
                dibujar_jugador(jugador_x, jugador_y)


def dibujar_jugador(x, y):
    canvas.create_oval(x * tamano, y * tamano, x * tamano + tamano, y * tamano + tamano, fill="blue", tags="jugador")


def dibujar_laberinto():
    for y in range(alto):
        for x in range(ancho):
            color = "white"
            if laberinto[y][x] == 1:
                color = "black"
            elif laberinto[y][x] == 2:
                color = "green"
            elif laberinto[y][x] == 3:
                color = "purple"
            elif laberinto[y][x] == 4:
                color = "orange"
            elif laberinto[y][x] == 111:
                color = "red"
            elif laberinto[y][x] == 587:
                messagebox.showwarning("Llegaste")
                
            canvas.create_rectangle(x * tamano, y * tamano, x * tamano + tamano, y * tamano + tamano, fill=color)

w.bind("<Key>", mover_jugador)

dibujar_laberinto()
dibujar_jugador(jugador_x, jugador_y)

w.mainloop()
