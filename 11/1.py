# Búsqueda en Arreglo Multidimensional

matriz = [
    [10, 25, 30],
    [5, 15, 35],
    [20, 40, 50]
]

def buscar_valor(matriz, valor):
    # Recorremos la matriz con dos bucles
    for i in range(len(matriz)):           # Recorre las filas
        for j in range(len(matriz[i])):    # Recorre las columnas
            if matriz[i][j] == valor:
                return True, (i, j)  # Devuelve True y la posición
    return False, None

# Valor a buscar
valor_a_buscar = 35

encontrado, posicion = buscar_valor(matriz, valor_a_buscar)

if encontrado:
    print(f"✅ El valor {valor_a_buscar} se encontró en la posición {posicion}.")
else:
    print(f"❌ El valor {valor_a_buscar} no se encontró en la matriz.")
