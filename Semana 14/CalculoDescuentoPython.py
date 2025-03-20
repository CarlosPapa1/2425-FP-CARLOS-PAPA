# Definición de la función con parámetro predeterminado
def calcular_descuento(monto_total, porcentaje_descuento=10):
    # Calcular el descuento
    descuento = monto_total * (porcentaje_descuento / 100)
    # Devolver el descuento
    return descuento

# Llamada a la función - solo monto total (usará el descuento predeterminado del 10%)
monto_1 = 80.0  # Cambié el monto a 300.0
descuento_1 = calcular_descuento(monto_1)
monto_final_1 = monto_1 - descuento_1
print(f"Compra 1: Monto total = ${monto_1}, Descuento = ${descuento_1}, Monto final a pagar = ${monto_final_1}")

# Llamada a la función - monto total + porcentaje de descuento personalizado
monto_2 = 50.0  # Cambié el monto a 500.0
descuento_personalizado = 20  # Cambié el porcentaje a 20%
descuento_2 = calcular_descuento(monto_2, descuento_personalizado)
monto_final_2 = monto_2 - descuento_2
print(f"Compra 2: Monto total = ${monto_2}, Descuento = ${descuento_2}, Monto final a pagar = ${monto_final_2}")
