class Puzzle8AStar:
    def __init__(self, estado_inicial, estado_meta):
        self.estado_inicial = estado_inicial
        self.estado_meta = estado_meta

    def obtener_movimientos(self, estado):
        movimientos = []
        espacio_vacio = estado.index(0)

        if espacio_vacio >= 3:
            nuevo_estado = estado[:]
            nuevo_estado[espacio_vacio], nuevo_estado[espacio_vacio - 3] = nuevo_estado[espacio_vacio - 3], nuevo_estado[espacio_vacio]
            movimientos.append(nuevo_estado)

        if espacio_vacio <= 5:
            nuevo_estado = estado[:]
            nuevo_estado[espacio_vacio], nuevo_estado[espacio_vacio + 3] = nuevo_estado[espacio_vacio + 3], nuevo_estado[espacio_vacio]
            movimientos.append(nuevo_estado)

        if espacio_vacio % 3 != 0:
            nuevo_estado = estado[:]
            nuevo_estado[espacio_vacio], nuevo_estado[espacio_vacio - 1] = nuevo_estado[espacio_vacio - 1], nuevo_estado[espacio_vacio]
            movimientos.append(nuevo_estado)

        if espacio_vacio % 3 != 2:
            nuevo_estado = estado[:]
            nuevo_estado[espacio_vacio], nuevo_estado[espacio_vacio + 1] = nuevo_estado[espacio_vacio + 1], nuevo_estado[espacio_vacio]
            movimientos.append(nuevo_estado)

        return movimientos

    def h(self, estado):
        """
        Función heurística: Distancia de Manhattan
        """
        distancia = 0
        for i in range(3):
            for j in range(3):
                valor = estado[i * 3 + j]
                if valor != 0:
                    fila_objetivo = (valor - 1) // 3
                    columna_objetivo = (valor - 1) % 3
                    distancia += abs(i - fila_objetivo) + abs(j - columna_objetivo)
        return distancia

    def resolver(self):
        frontera = [(self.h(self.estado_inicial), self.estado_inicial, [self.estado_inicial])]
        explorados = set()

        while frontera:
            _, estado, camino = frontera.pop(0)

            if estado == self.estado_meta:
                return camino

            explorados.add(tuple(estado))

            for movimiento in self.obtener_movimientos(estado):
                if tuple(movimiento) not in explorados:
                    nuevo_camino = camino + [movimiento]
                    frontera.append((self.h(movimiento) + len(nuevo_camino), movimiento, nuevo_camino))
                    frontera.sort()

        return None

    @staticmethod
    def dibujar_puzzle(estado):
        for i in range(3):
            for j in range(3):
                if estado[i * 3 + j] == 0:
                    print("|   ", end="")
                else:
                    print(f"| {estado[i * 3 + j]} ", end="")
            print("|")
            print("+---+---+---+")

estado_inicial = [8, 1, 0, 3, 4, 2, 5, 7, 6]
estado_meta = [1, 2, 3, 4, 5, 6, 7, 8, 0]

puzzle_solver = Puzzle8AStar(estado_inicial, estado_meta)
solucion = puzzle_solver.resolver()

if solucion:
    print("Se encontró una solución:")
    for paso, estado in enumerate(solucion):
        print(f"Paso {paso + 1}:")
        Puzzle8AStar.dibujar_puzzle(estado)
else:
    print("No se encontró una solución.")
