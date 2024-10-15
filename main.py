import numpy as np

#matriz para el laberinto
laberinto = np.array([
    [0, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0],
    [1, 0, 111, 0, 1, 0],  #trivia en 2-2
    [1, 1, 1, 1, 1, 0],
    [0, 0, 1, 0, 1, 0],
    [0, 1, 0, 0, 2, 0]  #salida en 5-4
])


direcciones = [(0, 1), (1, 0), (0, -1), (-1, 0)]  #derecha, abajo, izquierda y arriba
camino = []