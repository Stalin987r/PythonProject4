# ordenar_fila2.py

# Definimos una matriz 3x3 con valores numéricos
matriz = [
    [5, 8, 12],
    [3, 9, 7],
    [4, 6, 10]
]

# Función para ordenar una fila con Bubble Sort
def ordenar_fila(matriz, fila):
    n = len(matriz[fila])
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if matriz[fila][j] > matriz[fila][j + 1]:
                # Intercambio de elementos
                matriz[fila][j], matriz[fila][j + 1] = matriz[fila][j + 1], matriz[fila][j]
    return matriz

# Mostrar matriz original
print("📌 Matriz original:")
for f in matriz:
    print(f)

# Ordenamos la fila 2 (índice 1, porque Python empieza desde 0)
fila_a_ordenar = 1
matriz_ordenada = ordenar_fila(matriz, fila_a_ordenar)

# Mostrar matriz después de ordenar
print("\n📌 Matriz con la fila 2 ordenada en orden ascendente:")
for f in matriz_ordenada:
    print(f)
