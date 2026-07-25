'''
 EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
 '''

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def getNombre(self):
        return self.nombre

    def getEdad(self):
        return self.edad

    def saludar(self):
        print(f"Hola, soy {self.getNombre()}")

usuario1 = Persona("carmen", 22)

usuario1.saludar()

print(f"Edad: {usuario1.getEdad()}")



'''
 * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.

'''


class LIFO:
    def __init__(self):
        self.pila = []

    def añadirElemento(self, elemento):
        self.pila.append(elemento)

    def eliminarElemento(self):
        self.pila.pop()

    def imprimirPila(self):
        print(self.pila)

lifo1 = LIFO()
lifo1.imprimirPila()
lifo1.añadirElemento(1)
lifo1.imprimirPila()
lifo1.añadirElemento(2)
lifo1.imprimirPila()
lifo1.eliminarElemento()
lifo1.imprimirPila()


import queue

class FIFO:
    def __init__(self):
        self.cola = queue.Queue()

    def añadirElementoCola(self, elemento):
        self.cola.put(elemento)

    def eliminarElementoCola(self):
        self.cola.get()

    def imprimirCola(self):
        print(self.cola.queue)


cola1 = FIFO()
cola1.imprimirCola()
cola1.añadirElementoCola(1)
cola1.imprimirCola()
cola1.añadirElementoCola(2)
cola1.imprimirCola()
cola1.eliminarElementoCola()
cola1.imprimirCola()