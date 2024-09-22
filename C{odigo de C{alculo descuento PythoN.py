def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento aplicando el porcentaje al monto total de la compra.

    Args:
        monto_total (float): Monto total de la compra.
        porcentaje_descuento (int, optional): Porcentaje de descuento. Defaults to 10.

    Returns:
        float: Monto del descuento calculado.
    """
    descuento = (monto_total / 100) * porcentaje_descuento
    return descuento

