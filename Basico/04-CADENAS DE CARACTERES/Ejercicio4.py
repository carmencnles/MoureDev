'''
EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
 *   recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
 *   interpolación, verificación...
'''

s1 = "Hola"
s2 = "Python"

# Concatenación
print(s1 + "," + s2 + "!")

# Repetición
print(s1 * 3)

# Indexación 
print(s1[0] + s1[1] + s1[2] + s1[3])

# Longitud
print(len(s2)) 

# Slicing (porción) El indice final no se recoge.
print(s2[2:6])
print(s2[2:])
print(s2[:2])
print(s2[0:2])

# Busqueda
print("a" in s1)
print("y" in s2)

# Reemplazo
print(s1.replace("o", "a"))

# División
print(s2.split("t"))

# Mayusculas y minusculas
print(s1.upper())
print(s2.lower())
print("carmen canales".title())
print("carmen canales".capitalize())

# Eliminación de espacios al principio y al final
print(" carmen canales ".strip())

# Busqueda al principio y al final
print(s1.startswith("Ho"))
print(s2.startswith("Py"))
print(s1.endswith("Py"))
print(s2.endswith("thon"))


s3 = "Carmen Canales @carmencnles"


# Busqueda de posición
print(s3.find("carmen"))
print(s3.find("Carmen"))
print(s3.lower().find("Carmen"))

# Busqueda de ocurrencias
print(s3.lower().count("c"))

# Formateo
print("Saludo: {}, lenguaje: {}!".format(s1, s2))

# Interpolación
print(f"Saludo: {s1}, lenguaje: {s2}!")

# Transformación en lista de caracteres
print(list(s3))

s4 = [s1, ", ", s2, "!"]

# Transformación de lista en cadena
print("".join(s4))

# Transformaciones numericas
s5 = "123456"

s5 = float(s5)

print(s5)

# Comprobaciones varias
s5 = "123456"
print(s1.isalnum())
print(s1.isalpha())
print(s5.isalpha())
print(s5.isnumeric())


'''
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
'''

def check(word1, word2: str):
    
    # Palindromos - Dando la vuelta a la palabra, que sea la misma
    print(f"¿{word1} es un palindromo?  {word1 == word1[::-1]}")
    print(f"¿{word2} es un palindromo?  {word2 == word2[::-1]}")
    
    # Anagramas - Que entre dos palabras tengan las mismas letras pero en diferente orden
    print(f"¿{word1} es anagrama de {word2}?  {sorted(word1) == sorted(word2)}")

    # Isograma - Que las letras en una palabra aparezcan el mismo numero de veces
    print(f"¿{word1} es un isograma? {len(word1) == len(set(word1))}")
    print(f"¿{word2} es un isograma? {len(word2) == len(set(word2))}")

    # Isograma - 2º forma con función
    def isogram(word: str) -> bool:
        word_dict = dict()
        for word in word1:
            word_dict[word] = word_dict.get(word, 0) + 1
    
        isogram = True
        values = list(word_dict.values())
        isograma_len = values[0]
        for word_count in values:
            if word_count != isograma_len:
                isogram = False
                break

        return isogram

    print(f"¿{word1} es un isograma? {isogram(word1)}")
    print(f"¿{word2} es un isograma? {isogram(word2)}")


check("radar", "pythonpythonpython")
check("amor", "roma")

