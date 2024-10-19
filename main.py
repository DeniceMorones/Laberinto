import numpy as np
import tkinter as tk
from tkinter import simpledialog, messagebox
import random

ancho = 28
alto = 21
tamano = 25
dimension = 700

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
    [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
])

colores = {0: "white", 1: "black", 2: "blue", 3: "yellow", 4: "green", 111: "orange"}

for y in range(alto):
    for x in range(ancho):
        canvas.create_rectangle(
            x * tamano, y * tamano, x * tamano + tamano, y * tamano + tamano,
            fill=colores[laberinto[y, x]], outline="gray"
        )

jugador_pos = [0, 0]
jugador = canvas.create_oval(
    jugador_pos[1] * tamano + 2, jugador_pos[0] * tamano + 2,
    jugador_pos[1] * tamano + tamano - 2, jugador_pos[0] * tamano + tamano - 2,
    fill="red"
)

direcciones = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Derecha, Abajo, Izquierda, Arriba

visitadas = set()
visitadas.add((jugador_pos[0], jugador_pos[1]))

def manejar_teletransporte():
    jugador_pos[0], jugador_pos[1] = np.where(laberinto == 4)[0][0], np.where(laberinto == 4)[1][0]

def manejar_trivia():
    respuesta = simpledialog.askstring("Trivia", "¿Cuál es la capital de Francia?")
    if respuesta.lower() == "parís":
        messagebox.showinfo("Correcto", "¡Respuesta correcta!")
    else:
        messagebox.showinfo("Incorrecto", "Respuesta incorrecta. ¡Sigue intentándolo!")

def mover_jugador_auto():
    posibles_direcciones = []
    
    for direccion in direcciones:
        nueva_fila = jugador_pos[0] + direccion[0]
        nueva_columna = jugador_pos[1] + direccion[1]
        if 0 <= nueva_fila < alto and 0 <= nueva_columna < ancho and laberinto[nueva_fila, nueva_columna] != 1:
            if (nueva_fila, nueva_columna) not in visitadas:
                posibles_direcciones.append((nueva_fila, nueva_columna))

    if posibles_direcciones:
        nueva_fila, nueva_columna = random.choice(posibles_direcciones)
    else:
        while True:
            direccion = random.choice(direcciones)
            nueva_fila = jugador_pos[0] + direccion[0]
            nueva_columna = jugador_pos[1] + direccion[1]
            if 0 <= nueva_fila < alto and 0 <= nueva_columna < ancho and laberinto[nueva_fila, nueva_columna] != 1:
                break
    
    jugador_pos[0], jugador_pos[1] = nueva_fila, nueva_columna
    visitadas.add((nueva_fila, nueva_columna))
    canvas.coords(jugador,
                  jugador_pos[1] * tamano + 2, jugador_pos[0] * tamano + 2,
                  jugador_pos[1] * tamano + tamano - 2, jugador_pos[0] * tamano + tamano - 2)

    if laberinto[nueva_fila, nueva_columna] == 111:
        manejar_trivia()

    if laberinto[nueva_fila, nueva_columna] == 3:
        manejar_teletransporte()

    w.after(300, mover_jugador_auto)  # Mover cada 300 ms (lento)

mover_jugador_auto()

w.mainloop()
