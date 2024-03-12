import pygame
import numpy as np
import time 

pygame.init()

width, height = 450, 450
screen = pygame.display.set_mode((height, width))
bg = 25, 25, 25
screen.fill(bg)

# Numero de celdas
nxC, nyC = 25, 25
# Dimensiones de las celdas
dimCW = width / nxC
dimCH = height / nyC

# Estados de las celdas
gameState = np.zeros((nxC, nyC))

gameState[5, 3] = 1
gameState[5, 4] = 1
gameState[5, 5] = 1

gameState[21, 21] = 1
gameState[22, 22] = 1
gameState[22, 23] = 1
gameState[21, 23] = 1
gameState[20, 23] = 1

# Bucle de ejecucion
while True:

    newGameState = np.copy(gameState)

    screen.fill(bg)
    time.sleep(0.1)
    for y in range(0, nxC):
        for x in range(0, nyC):

            # Numero de vecinos
            n_neigh = gameState[(x - 1) % nxC, (y - 1) % nyC] + \
                      gameState[(x - 1) % nxC, y % nyC] + \
                      gameState[(x - 1) % nxC, (y + 1) % nyC] + \
                      gameState[x % nxC, (y - 1) % nyC] + \
                      gameState[x % nxC, (y + 1) % nyC] + \
                      gameState[(x + 1) % nxC, (y - 1) % nyC] + \
                      gameState[(x + 1) % nxC, y % nyC] + \
                      gameState[(x + 1) % nxC, (y + 1) % nyC]

            # Regla1: Una celda muerta con exactamente 3 vecinas vivas se convierte en una celda viva.
            if gameState[x, y] == 0 and n_neigh == 3:
                newGameState[x, y] = 1

            # Regla2: Una celda viva con menos de 2 vecinas vivas (soledad) o más de 3 vecinas vivas (sobrepoblación) muere.
            elif gameState[x, y] == 1 and (n_neigh < 2 or n_neigh > 3):
                newGameState[x, y] = 0

            # Poligono de cada celda
            poly = [((x) * dimCW, y * dimCH),
                    ((x + 1) * dimCW, y * dimCH),
                    ((x + 1) * dimCW, (y + 1) * dimCH),
                    ((x) * dimCW, (y + 1) * dimCH)]

            if newGameState[x, y] == 0:
                pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
            else:
                pygame.draw.polygon(screen, (255, 255, 255), poly, 0)

    # Actualizamos el estado del juego
    gameState = np.copy(newGameState)

    pygame.display.flip()

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
