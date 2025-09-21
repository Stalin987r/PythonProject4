# Función para calcular el descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el monto del descuento aplicando un porcentaje al monto total de la compra.

    Parámetros:
    monto_total (float): Monto total de la compra
    porcentaje_descuento (float, opcional): Porcentaje de descuento a aplicar. Valor por defecto = 10

    Retorna:
    float: Monto del descuento calculado
    """
    descuento = monto_total * (porcentaje_descuento / 100)  # Calcula el descuento
    return descuento  # Devuelve el monto del descuento


# ------------------ PROGRAMA PRINCIPAL ------------------

# Primera llamada: solo con el monto total (usa el 10% por defecto)
monto1 = 200
descuento1 = calcular_descuento(monto1)  # Aquí solo se pasa el monto
final1 = monto1 - descuento1  # Monto final después del descuento

# Segunda llamada: con monto total y porcentaje de descuento específico
monto2 = 500
descuento2 = calcular_descuento(monto2, 20)  # Aquí pasamos el monto y el 20% de descuento
final2 = monto2 - descuento2  # Monto final después del descuento

# ------------------ SALIDA DE RESULTADOS ------------------

print("Compra 1 (descuento por defecto 10%):")
print(f" Monto total: ${monto1}")
print(f" Descuento aplicado: ${descuento1}")
print(f" Monto final a pagar: ${final1}\n")

print("Compra 2 (descuento personalizado 20%):")
print(f" Monto total: ${monto2}")
print(f" Descuento aplicado: ${descuento2}")
print(f" Monto final a pagar: ${final2}")

