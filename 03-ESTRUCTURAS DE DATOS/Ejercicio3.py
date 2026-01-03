'''
EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto
 *   en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 '''


lista = [1, "hola", 3.14]

lista2 = ["a", "ddddd", "aaaa", "x", "b"]

tupla = (1, "hola", 3.14)

diccionario = {"clave1":"hola","clave2":2,"clave3":3.14}


# Lista
# Inserción
lista.append("hola2")

# Añade en una posicion en concreto

lista.insert(1, 7)

print(lista)
# Eliminar

lista.remove("hola2")

print(lista)

# Elimina y devuelve un elemento por el indice

print(lista.pop(2))
#print(lista)

# Ordena la lista

print("Lista2 ordenada: ")
lista2.sort()
print(lista2)

# Tupla - No se puede modificar, pero si iterar

print(tupla[2])


# Diccionario
# Bucles para mostrar

# Muestra la clave del diccionario, en este caso lo interpreta.
for clave in diccionario:
    print(clave)

# Muestra los valores especificando .values
for valor in diccionario.values():
    print(valor)

# Muestra los pares de clave-valor especificando .items
for valor in diccionario.items():
    print(valor)

# Numero de elementos que tiene el diccionario
print(len(diccionario))

# Eliminar elemento clave-valor de diccionario
del diccionario["clave1"]

print(diccionario)

# Devuelve elemento clave-valor del diccionario y muestra el valor eliminado
print(diccionario.pop("clave2"))

print(diccionario)

# Vacia el diccionario
diccionario.clear()

print(diccionario)


'''
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
 '''


agenda = {"Pablo":624224427,"Carmen":621233427,"Pedro":621263457}


def insertar_agenda():
    
    nombre = input("Introduce un nombre: ")
    numero = int(input("Introduce un numero de telefono: ")) 

    agenda[nombre] = numero

    return agenda

# De esta manera meto a pelo los dos parametros, no pido por terminal nada.

'''
def insertar_agenda(nombre, numero):
    
    print(f"La agenda actual es: {agenda}")  

    agenda[nombre] = numero

    return agenda
'''  

# Si elimino nombre = input("Introduce un valor: ") y añado un parametro como en el 1. lo meteria a pelo,
# si no, buscaria con el nombre que meto por terminal.

def buscar_agenda():

    nombre = int(input("Introduce un valor: "))

    if nombre in agenda:
        print("Existe el valor.")
    else:
        print("No existe el valor proporcionado.")


def actualizar_agenda():
    print(agenda)
    nombre = input("Introduce la clave del valor a modificar: ")
    if nombre in agenda:
        print("Existe el valor.")
        numero = int(input("Introduce un numero de telefono a actualizar: "))
        agenda[nombre] = numero
    else:
        print("No existe, no puedes actualizarlo.")



def eliminar_agenda():

    print(agenda)
    nombre = input("Introduce la clave del par clave-valor a eliminar: ")
    if nombre in agenda:
        print("Existe el valor.")

        del agenda[nombre]
        print(agenda)
    else:
        print("No existe, no puedes eliminarlo.")


while True:
    print("""Introduce una opción de las siguientes:
    
    1. Insertar contacto")
    2. Buscar contacto")
    3. Actualización de contacto")
    4. Eliminar contacto")
    Salir.""")
    opcion = input("Opción: ")
    if opcion == "1":

        insertar_agenda()

        print(agenda)

    if opcion == "2":

        buscar_agenda()

    if opcion == "3":

        actualizar_agenda()
    
    if opcion == "4":

        eliminar_agenda()
    
    if opcion == "5":

        break

print("Cerrando programa...")




