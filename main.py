import numpy as np
import tkinter as tk

ancho = 28 
alto = 28   
tamano = 25  
dimension = 650


w = tk.Tk()
w.title("Laberinto")
canvas = tk.Canvas(w, width=dimension, height=dimension, bg="white")
canvas.pack()


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
    [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
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
    "a": (-1, 0),  # Iz
    "d": (1, 0)    # De
}

# Posición inicial del jugador
jugador_x, jugador_y = 0, 0


def dibujar_laberinto():
    for i in range(ancho):
        for j in range(alto):
            x1 = i * tamano
            y1 = j * tamano
            x2 = x1 + tamano
            y2 = y1 + tamano
            if laberinto[j][i] == 1:  
                canvas.create_rectangle(x1, y1, x2, y2, fill="black")  # Muros
            else:
                canvas.create_rectangle(x1, y1, x2, y2, fill="white")  # Caminos


def dibujar_entrada():
    x1 = 0 * tamano
    y1 = 0 * tamano
    x2 = x1 + tamano
    y2 = y1 + tamano
    canvas.create_rectangle(x1, y1, x2, y2, fill="green", outline="green")  # Entrada

def dibujar_salida():
    x1 = 25 * tamano
    y1 = 24 * tamano
    x2 = x1 + tamano
    y2 = y1 + tamano
    canvas.create_rectangle(x1, y1, x2, y2, fill="red", outline="red")  # Salida

def dibujar_jugador(x, y):
    x1 = x * tamano
    y1 = y * tamano
    x2 = x1 + tamano
    y2 = y1 + tamano
    return canvas.create_rectangle(x1, y1, x2, y2, fill="purple", outline="purple", tags="jugador")


def mover_jugador(event):
    global jugador_x, jugador_y

    
    if event.char in direcciones:
        dx, dy = direcciones[event.char]
        nuevo_x, nuevo_y = jugador_x + dx, jugador_y + dy

        # posición es válida (no es un muro)
        if 0 <= nuevo_x < ancho and 0 <= nuevo_y < alto and laberinto[nuevo_y][nuevo_x] == 0:
            # Borrar la posición anterior 
            canvas.delete("jugador")
            
            # Actualiza la nueva posición 
            jugador_x, jugador_y = nuevo_x, nuevo_y
            
            # jugador en la nueva posición
            dibujar_jugador(jugador_x, jugador_y)

dibujar_laberinto()
dibujar_entrada()  
dibujar_salida()   


dibujar_jugador(jugador_x, jugador_y)

# teclas para mover al jugador
w.bind("<KeyPress>", mover_jugador)

w.mainloop()
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
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0],
    [1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0],
    [1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 111, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 4 , 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0],
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

# Buscar automáticamente la posición de la salida
pos_salida = np.where(laberinto == 2)
fila_salida, columna_salida = pos_salida[0][0], pos_salida[1][0]

def mover_jugador_auto():
    posibles_direcciones = []
    
    # Buscar direcciones posibles no visitadas
    for direccion in direcciones:
        nueva_fila = jugador_pos[0] + direccion[0]
        nueva_columna = jugador_pos[1] + direccion[1]
        if 0 <= nueva_fila < alto and 0 <= nueva_columna < ancho and laberinto[nueva_fila, nueva_columna] != 1:
            if (nueva_fila, nueva_columna) not in visitadas:
                posibles_direcciones.append((nueva_fila, nueva_columna))

    if posibles_direcciones:
        # Prioriza las direcciones no visitadas
        nueva_fila, nueva_columna = random.choice(posibles_direcciones)
    else:
        # Retrocede si no hay direcciones nuevas, pero evita movimientos repetitivos
        posibles_direcciones = [
            (jugador_pos[0] + direccion[0], jugador_pos[1] + direccion[1])
            for direccion in direcciones
            if 0 <= jugador_pos[0] + direccion[0] < alto and 
               0 <= jugador_pos[1] + direccion[1] < ancho and 
               laberinto[jugador_pos[0] + direccion[0], jugador_pos[1] + direccion[1]] != 1
        ]

        if posibles_direcciones:
            nueva_fila, nueva_columna = random.choice(posibles_direcciones)
    
    # Actualizar la posición del jugador y añadir la nueva posición a visitadas
    jugador_pos[0], jugador_pos[1] = nueva_fila, nueva_columna
    visitadas.add((nueva_fila, nueva_columna))

    # Actualizar la posición visual del jugador en el canvas
    canvas.coords(jugador,
                  jugador_pos[1] * tamano + 2, jugador_pos[0] * tamano + 2,
                  jugador_pos[1] * tamano + tamano - 2, jugador_pos[0] * tamano + tamano - 2)

    # Verificar si ha llegado a la salida
    if nueva_fila == fila_salida and nueva_columna == columna_salida:
        messagebox.showinfo("Salida", "¡Has llegado a la salida!")
        return  # Detener el movimiento después de llegar a la salida
    
    # Manejar eventos especiales
    if laberinto[nueva_fila, nueva_columna] == 111:
        manejar_trivia()

    if laberinto[nueva_fila, nueva_columna] == 3:
        manejar_teletransporte()

    # Mover automáticamente después de un tiempo (300 ms)
    w.after(300, mover_jugador_auto)

# Iniciar movimiento automático
mover_jugador_auto()

w.mainloop()
