# Ejercicio 1: Suma de elementos en una lista de listas
def suma_matriz(matriz):

    filas = len(matriz)
    columnas = len(matriz[0])
    suma = 0
    for i in range(filas):
        for j in range(columnas):
            suma += matriz[i][j]
    return suma

# Ejercicio 2: Encontrar el valor máximo en una matriz
def maximo_matriz(matriz):
    """
    Recibe una lista de listas y devuelve el valor máximo.
    Incluir el código aquí para encontrar el valor máximo en la matriz.
    """
    filas = len(matriz)
    columnas = len(matriz[0])
    max = matriz[0][0]
    for i in range(filas):
        for j in range(columnas):
            if matriz[i][j] > max:
                max = matriz[i][j]
    return max
# Ejercicio 3: Verificar si un número es primo
def es_primo(n):

    if n <= 1:
        return False
    
    for i in range(2,n):
        if  n % i == 0:
            return False
    else:
        return True
    
        
es_primo(1)

# Ejercicio 4: Transponer una matriz
def transponer_matriz(matriz):

    filas = len(matriz)
    columnas = len(matriz[0])

    transpuesta = []
    for i in range(columnas):
        fila = [0] * filas
        transpuesta += [fila]

    for i in range(filas):
        for j in range(columnas):
            transpuesta[j][i] = matriz[i][j]
    return transpuesta


# Ejercicio 5: Filtrar números pares
def filtrar_pares(lista):

    num_pares = []
    for numero in lista:
        if numero % 2 == 0:
            num_pares.append(numero)
    return num_pares



# Ejercicio 6: Contar la cantidad de palabras en una frase
def contar_palabras(frase):

    letras = frase.split()
    palabras= len(letras)
    return palabras



# Ejercicio 7: Crear una tabla de multiplicar
def tabla_multiplicar(n):

    tabla = []
    for i in range(1,11):
        tabla.append(n * i)
    return tabla

# Ejercicio 8: Contar números negativos en una lista
def contar_negativos(lista):

    contador = 0
    for numero in lista:
        if numero < 0:
            contador += 1
    return contador

# Ejercicio 9: Determinar si una lista está ordenada
def lista_ordenada(lista):

    contar = len(lista)-1
    for i in range(contar):
        if lista[i] > lista[i + 1]:
            return False
    return True


    

# Ejercicio 10: Cifrar un texto con el cifrado César
def cifrado_cesar(texto, desplazamiento):

    palabras = ""
    for letra in texto:
        codigo = ord(letra) + desplazamiento
        cesar = chr(codigo)
        palabras += cesar
    return palabras

#Aquí comienza el progrma principal. No modifiques el código debajo de esta línea.
def main():
    pass


if __name__ == "__main__":
    main()
