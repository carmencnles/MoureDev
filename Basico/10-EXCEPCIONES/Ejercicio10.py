'''
 EJERCICIO:
 * Explora el concepto de manejo de excepciones según tu lenguaje.
 * Fuerza un error en tu código, captura el error, imprime dicho error
 * y evita que el programa se detenga de manera inesperada.
 * Prueba a dividir "10/0" o acceder a un índice no existente
 * de un listado para intentar provocar un error.
'''

#print(10/0)

try:

    print(10/0)
    my_list = [1,2,3,4]
    print(my_list[4])

except ZeroDivisionError as e: # except Exception as e:
    print(f"Se ha producido un error: {e} ({type(e).__name__})")

'''
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que sea capaz de procesar parámetros, pero que también
 * pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
 * corresponderse con un tipo de excepción creada por nosotros de manera
 * personalizada, y debe ser lanzada de manera manual) en caso de error.
 * - Captura todas las excepciones desde el lugar donde llamas a la función.
 * - Imprime el tipo de error.
 * - Imprime si no se ha producido ningún error.
 * - Imprime que la ejecución ha finalizado.
'''

print("Dificultad extra:")

# Excepcion personalizada, creada por mi misma.
class StrTypeError(Exception):
    pass

def process_params(parameters: list):

    if len(parameters) < 3:
        raise IndexError()
    elif parameters[1] == 0:
        raise ZeroDivisionError()
    elif type(parameters[2]) == str:
        raise StrTypeError("El tercer elemento no puede ser una cadena de texto")
    
    print(parameters[2])
    print(parameters[0]/parameters[1])
    print(parameters[2] + 5)

try:
    process_params([1,2,3,4])
except IndexError as e:
    print("El numero de elementos de la lista debe ser mayor que dos")
except ZeroDivisionError as e:
    print("El segundo elemento de la lista no puede ser un cero")
except StrTypeError as e:
    print(f"{e}")
except Exception as e:
    print(f"Se ha producido un error inesperado {e}")
else: #Este else lo imprime en caso de que no se produzcan ninguno de los errores anteriores
    print("No se ha producido ningun error")
finally: # Al agregar el finally, se ejecuta pase lo que pase.
    print("El programa finaliza sin detenerse")
