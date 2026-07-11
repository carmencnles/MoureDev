'''
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
'''

#Operadores Aritméticos -> +, -, *, /, %, **, //
#Operadores Relacionales -> >, <, ==, >=, <=, !=
#Operadores Bit a Bit -> &, |, ^, ~, >>, <<
#Operadores de Asignación -> =, +=, -=, *=, /=, %=, **=, //=, &=,|=	, ^=, >>=, <<=
#Operadores Lógicos -> and, or, not
#Operadores de Pertenencia -> in, not in
#Operadores de Identidad -> is, is not


#Operadores aritmeticos
n1 = 1
n2 = 2 
n3 = 3
print(f'Suma de {n1} + {n2} = {n3}')

print(f"La suma de 4 + 3 =  {4 + 3}")
print(f"La resta de 4 - 3 =  {4 - 3}")
print(f"La multiplicacion de 4 * 3 =  {4 * 3}")
print(f"La división de 4 / 3 =  {4 / 3}")
print(f"La división de 4 % 3 =  {4 % 3}")
print(f"La exponente de 4 ** 3 =  {4 ** 3}")
print(f"La división entera de 4 // 3 =  {4 // 3}")

#Operadores de comparación/relaciones
print(f"Igualdad: 10 == 3 es {10 == 3}")
print(f"Desigualdad: 10 != 3 es {10 != 3}")
print(f"Mayor que: 10 > 3 es {10 > 3}")
print(f"Menor que: 10 < 3 es {10 < 3}")
print(f"Mayor o igual que: 10 >= 3 es {10 >= 3}")
print(f"Menor o igual que: 10 <= 3 es {10 <= 3}")

#Operadores logicos

print(f"AND &&: 10 + 3 == 13 and 5 - 1 == 4 es {10 + 3 == 13 and 5 - 1 == 4}" )
print(f"OR ||: 10 + 3 == 14 and 5 - 1 == 5 es {10 + 3 == 14 and 5 - 1 == 5}" )
print(f"NOT !: not 10 + 3 == 14 es {not 10 + 3 == 14}" )

#Operadores de asignación

my_number = 11 # asignación
my_number += 11 # suma y asignación
my_number -= 11 # resta y asignación
my_number *= 11 # multiplicación y asignación
my_number /= 11 # división y asignación
my_number %= 11 # modulo y asignación
my_number **= 11 # exponente y asignación
my_number //= 11 # división entera y asignación

#Operadores de identidad

my_new_number = my_number
my_new_number = 1.0
print(f"my_number is my_new_number es {my_number is my_new_number}")
print(f"my_number is my_new_number es {my_number is not my_new_number}")

#Operadores de pertenencia

print(f"'c' in 'carmen' =  {'c' in 'carmen'}")
print(f"'c' in 'carmen' =  {'c' not in 'carmen'}")

#Operadores de bit

a = 10
b = 3

print(f"AND: 10 & 3 = {10 & 3}")
print(f"OR: 10 | 3 = {10 | 3}")
print(f"XOR: 10 ^ 3 = {10 ^ 3}")
print(f"NOT: -10 = {-10}")
print(f"Desplazamiento a la derecha: 10 >> 2 {10 >> 2}")
print(f"Desplazamiento a la izquierda: 10 >> 2 {10 << 2}")

#ESTRUCTURAS DE CONTROL


#Condicionales

my_string = "Carmencnles"

if my_string == 'Carmencnles':
    print("my_string es Carmencnles")
elif my_string == "Carmen":
    print("my_string es 'Carmen'")
else: 
    print("my_string no es 'Carmencnles'")

#Iterativas

for i in range(11):
    print(i)


i = 0

while i <= 10:
    print(i)
    i += 1 


#Manejo de excepciones

try:
    print(10 / 0)
except:
    print("Se ha producido un error")
finally:
    print("Ha finalizado el manejo de excepciones")


#Crea un programa que imprima por consola todos los números comprendidos
#* entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

for i in range(10, 56, 2):
    if i % 3 != 0 and i != 16:
        print(i)

