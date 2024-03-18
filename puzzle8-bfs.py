from queue import Queue

class Puzzle8:
    def __init__(self, estado_inicial, estado_meta):
        self.estado_inicial = estado_inicial
        self.estado_meta = estado_meta
        self.cola = Queue()
        self.visitados = []

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

    def busqueda_amplitud(self):
        self.cola.put((self.estado_inicial, []))

        while not self.cola.empty():
            estado, path = self.cola.get()
            self.visitados.append(estado)

            if estado == self.estado_meta:
                return path

            for movimiento in self.obtener_movimientos(estado):
                if movimiento not in self.visitados:
                    self.cola.put((movimiento, path + [movimiento]))

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

estado_inicial = [8,1,0,3,4,2,5,7,6]
estado_meta = [1, 2, 3, 4, 5, 6, 7, 8, 0]

puzzle_solver = Puzzle8(estado_inicial, estado_meta)
solucion = puzzle_solver.busqueda_amplitud()

if solucion:
    print("Se encontró una solución:")
    for paso, estado in enumerate(solucion):
        print(f"Paso {paso + 1}:")
        Puzzle8.dibujar_puzzle(estado)
else:
    print("No se encontró una solución.")
