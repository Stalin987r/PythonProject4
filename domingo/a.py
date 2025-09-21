# Programa: Búsqueda en una matriz bidimensional (3x3)

# Definir matriz 3x3 con valores numéricos
matriz = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

# Función para buscar un valor en la matriz
def buscar_valor(matriz, valor):
    for i in range(len(matriz)):          # recorrer filas
        for j in range(len(matriz[i])):   # recorrer columnas
            if matriz[i][j] == valor:
                return (i, j)  # retorna la posición (fila, columna)
    return None

# Valor a buscar
valor_buscado = 50

# Mostrar la matriz original
print("Matriz:")
for fila in matriz:
    print(fila)

# Buscar valor
posicion = buscar_valor(matriz, valor_buscado)

if posicion:
    print(f"\n✅ El valor {valor_buscado} se encontró en la posición: fila {posicion[0]}, columna {posicion[1]}")
else:
    print(f"\n❌ El valor {valor_buscado} no se encuentra en la matriz.")
