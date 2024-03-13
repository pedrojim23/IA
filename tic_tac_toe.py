import math

# Representación del tablero
board = [[' ' for _ in range(3)] for _ in range(3)]

# Función para imprimir el tablero
def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

# Función para verificar si hay un ganador
def check_winner(board, player):
    # Verificar filas y columnas
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    # Verificar diagonales
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Función para verificar si el juego ha terminado en empate
def check_draw(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

# Función para realizar un movimiento
def make_move(board, row, col, player):
    if board[row][col] == ' ':
        board[row][col] = player
    else:
        print("¡Esa casilla ya está ocupada! Por favor, elige otra.")
        return False
    return True


# Función para obtener la lista de movimientos disponibles
def get_available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

# Función Minimax
def minimax(board, depth, maximizing_player):
    # Si 'O' gana, devuelve 1 (máxima puntuación)
    if check_winner(board, 'O'):
        return 1
    # Si 'X' gana, devuelve -1 (mínima puntuación)
    elif check_winner(board, 'X'):
        return -1
    # Si el juego termina en empate, devuelve 0
    elif check_draw(board):
        return 0

    if maximizing_player:  # Si es el turno de maximizar el puntaje (jugador 'O')
        max_eval = -math.inf  # Inicializa el puntaje máximo como negativo infinito
        # Itera a través de los movimientos disponibles
        for move in get_available_moves(board):
            row, col = move
            board[row][col] = 'O'  # Intenta realizar el movimiento para 'O'
            # Llama recursivamente a minimax para evaluar el siguiente movimiento del oponente ('X')
            eval = minimax(board, depth + 1, False)
            board[row][col] = ' '  # Deshace el movimiento para explorar otras posibilidades
            max_eval = max(max_eval, eval)  # Actualiza el puntaje máximo encontrado
        return max_eval  # Devuelve el puntaje máximo encontrado
    else:  # Si es el turno de minimizar el puntaje (jugador 'X')
        min_eval = math.inf  # Inicializa el puntaje mínimo como infinito
        # Itera a través de los movimientos disponibles
        for move in get_available_moves(board):
            row, col = move
            board[row][col] = 'X'  # Intenta realizar el movimiento para 'X'
            # Llama recursivamente a minimax para evaluar el siguiente movimiento de la computadora ('O')
            eval = minimax(board, depth + 1, True)
            board[row][col] = ' '  # Deshace el movimiento para explorar otras posibilidades
            min_eval = min(min_eval, eval)  # Actualiza el puntaje mínimo encontrado
        return min_eval  # Devuelve el puntaje mínimo encontrado

# Función para encontrar el mejor movimiento usando el algoritmo Minimax
def find_best_move(board):
    # Inicializa la variable para el mejor puntaje con un valor muy bajo
    best_eval = -math.inf
    # Inicializa la variable para el mejor movimiento como None
    best_move = None
    # Itera sobre todos los movimientos disponibles en el tablero
    for move in get_available_moves(board):
        # Obtiene la fila y columna del movimiento actual
        row, col = move
        # Realiza el movimiento en el tablero simulando que la computadora juega como 'O'
        board[row][col] = 'O'
        # Calcula el puntaje usando el algoritmo Minimax para el movimiento actual
        eval = minimax(board, 0, False)
        # Deshace el movimiento para explorar otras posibilidades
        board[row][col] = ' '
        # Compara el puntaje obtenido con el mejor puntaje encontrado hasta ahora
        if eval > best_eval:
            # Si el puntaje es mejor que el mejor puntaje actual, actualiza el mejor puntaje y el mejor movimiento
            best_eval = eval
            best_move = move
    # Devuelve el mejor movimiento encontrado
    return best_move


# Función principal del juego
def play_game():
    print("Bienvenido al juego Tic-Tac-Toe con Minimax!")
    print_board(board)
    while not check_winner(board, 'O') and not check_winner(board, 'X') and not check_draw(board):
        # Turno del jugador X
        while True:
            row = int(input("Fila (0, 1, 2) para Y: "))
            col = int(input("Columna (0, 1, 2) para X: "))
            if make_move(board, row, col, 'X'):
                break
        print_board(board)
        if check_winner(board, 'X'):
            print("¡Felicidades! ¡Has ganado!")
            break
        elif check_draw(board):
            print("¡El juego terminó en empate!")
            break
        # Turno de la computadora O
        print("Turno de la computadora (O)...")
        row, col = find_best_move(board)
        make_move(board, row, col, 'O')
        print(f"La computadora (O) ha elegido la fila {row} y la columna {col}")
        print_board(board)
        if check_winner(board, 'O'):
            print("¡La computadora ha ganado!")
            break
        elif check_draw(board):
            print("¡El juego terminó en empate!")
            break

# Llama a la función principal para comenzar el juego
play_game()
