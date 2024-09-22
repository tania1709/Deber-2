# Monto total y descuento
def calcular_descuento(monto_total, porcentaje_descuento):
    # Validación de porcentaje de descuento
    if porcentaje_descuento < 0 or porcentaje_descuento > 100:
        raise ValueError("Porcentaje de descuento inválido")

    descuento = (monto_total / 100) * porcentaje_descuento
    return descuento

monto_total = float(input("Ingrese el monto total: $"))
porcentaje_descuento = int(input("Ingrese el porcentaje de descuento (%): "))

try:
    descuento_calculado = calcular_descuento(monto_total, porcentaje_descuento)
    monto_final = monto_total - descuento_calculado

    print(f"Monto total: ${monto_total:.2f}")
    print(f"Porcentaje de descuento: {porcentaje_descuento}%")
    print(f"Descuento calculado: ${descuento_calculado:.2f}")
    print(f"Monto final: ${monto_final:.2f}")
except ValueError as e:
    print(e)












