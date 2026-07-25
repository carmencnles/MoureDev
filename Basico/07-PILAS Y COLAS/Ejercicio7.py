'''
EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
 '''

import queue

q1 = queue.Queue()


q1.put(1)
q1.put(5)
q1.put(7)
q1.put(9)
q1.put(10)

print(q1.full())

#print(type(q1))

item1 = q1.get()

print('The item removed from the queue is ', item1)

item2 = q1.get()

print('The item removed from the queue is ', item2)


lista = []

lista.append(50)
lista.append(30)
lista.append(20)
lista.append(10)

ultimo = lista.pop()
print(f"Saco el {ultimo}")

print("Pila después de sacar un libro de la caja:", lista)

'''
 * DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.

'''