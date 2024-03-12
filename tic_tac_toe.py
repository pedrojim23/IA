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
    if check_winner(board, 'O'):
        return 1
    elif check_winner(board, 'X'):
        return -1
    elif check_draw(board):
        return 0
    
    if maximizing_player:
        max_eval = -math.inf
        for move in get_available_moves(board):
            row, col = move
            board[row][col] = 'O'
            eval = minimax(board, depth + 1, False)
            board[row][col] = ' '
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        for move in get_available_moves(board):
            row, col = move
            board[row][col] = 'X'
            eval = minimax(board, depth + 1, True)
            board[row][col] = ' '
            min_eval = min(min_eval, eval)
        return min_eval

# Función para encontrar el mejor movimiento usando el algoritmo Minimax
def find_best_move(board):
    best_eval = -math.inf
    best_move = None
    for move in get_available_moves(board):
        row, col = move
        board[row][col] = 'O'
        eval = minimax(board, 0, False)
        board[row][col] = ' '
        if eval > best_eval:
            best_eval = eval
            best_move = move
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
