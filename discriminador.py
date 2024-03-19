from experta import *

# Definimos la clase Animales que hereda de KnowledgeEngine (un motor de reglas).
class Animales(KnowledgeEngine):
        # Regla: Si un animal tiene dientes afilados, garras y ojos mirando hacia adelante, entonces es carnívoro.
        @Rule(OR(AND(Fact('dientes afilados'),Fact('garras'),Fact('ojos mirando hacia adelante')),Fact('come carne')))
        def carnivoro(self):
                self.declare(Fact('carnívoro'))
        # Regla: Si un animal tiene pelaje o da leche, entonces es un mamífero.
        @Rule(OR(Fact('pelaje'),Fact('da leche')))
        def mamifero(self):
                self.declare(Fact('mamífero'))

        @Rule(Fact('mamífero'),OR(Fact('tiene pezuñas'),Fact('rumia')))
        def pezunas(self):
                self.declare(Fact('ungulado'))

        @Rule(OR(Fact('plumas'),AND(Fact('vuela'),Fact('pone huevos'))))
        def ave(self):
                self.declare(Fact('ave'))

        # Reglas para animales específicos:
        # Si un animal es mamífero, carnívoro, tiene color rojo-marrón y patrones de rayas oscuras, entonces es un tigre.
        @Rule(Fact('mamífero'),Fact('carnívoro'),Fact(color='rojo-marrón'),Fact(pattern='manchas oscuras'))
        def mono(self):
                self.declare(Fact(animal='mono'))

        @Rule(Fact('mamífero'),Fact('carnívoro'),Fact(color='rojo-marrón'),Fact(pattern='rayas oscuras'))
        def tigre(self):
                self.declare(Fact(animal='tigre'))

        @Rule(Fact('ungulado'),Fact('cuello largo'),Fact('patas largas'),Fact(pattern='manchas oscuras'))
        def jirafa(self):
                self.declare(Fact(animal='jirafa'))

        @Rule(Fact('ungulado'),Fact(pattern='rayas oscuras'))
        def cebra(self):
                self.declare(Fact(animal='cebra'))

        @Rule(Fact('ave'),Fact('cuello largo'),Fact('no puede volar'),Fact(color='negro y blanco'))
        def avestruz(self):
                self.declare(Fact(animal='avestruz'))

        @Rule(Fact('ave'),Fact('nada'),Fact('no puede volar'),Fact(color='negro y blanco'))
        def pinguino(self):
                self.declare(Fact(animal='pingüino'))

        @Rule(Fact('ave'),Fact('vuela bien'))
        def albatros(self):
                self.declare(Fact(animal='albatros'))

        # Método para imprimir el resultado final.
        @Rule(Fact(animal=MATCH.a))
        def imprimir_resultado(self, a):
                print('El animal es {}'.format(a))

        @Rule(Fact('mamífero'), Fact('come hierbas'))
        def herbivoro(self):
                self.declare(Fact('herbívoro'))

        @Rule(Fact('herbívoro'), Fact('cuello largo'))
        def jirafa_herbivora(self):
                self.declare(Fact(animal='jirafa herbívora'))

        @Rule(Fact('herbívoro'), Fact('rayas blancas y negras'))
        def cebra_herbivora(self):
                self.declare(Fact(animal='cebra herbívora'))

        @Rule(Fact('ave'), Fact('pico largo'))
        def tucan(self):
                self.declare(Fact(animal='tucán'))

        @Rule(Fact('ave'), Fact('nada'), Fact('colorido'))
        def pez_pajaro(self):
                self.declare(Fact(animal='pez pájaro'))

        # Método para establecer múltiples hechos a la vez.
        def hechos(self, l):
                for x in l:
                        self.declare(x)

# Creamos una instancia de la clase Animales.
ex1 = Animales()
ex1.reset()
# Establecemos los hechos iniciales sobre un animal.
ex1.hechos([
    Fact(color='rojo-marrón'),
    Fact(pattern='rayas oscuras'),
    Fact('dientes afilados'),
    Fact('garras'),
    Fact('ojos mirando hacia adelante'),
    Fact('da leche')])
# Ejecutamos el motor de reglas para clasificar el animal.
ex1.run()
ex1.facts
