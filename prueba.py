def calcular_precio_final(precio_base, es_miembro, tiene_cupon):
    # Complejidad inicial = 1
    descuento = 0
    
    # +1 por el primer 'if'
    if es_miembro:
        descuento = 0.20  # 20% de descuento
    
    # +1 por el segundo 'if'
    elif tiene_cupon:
        descuento = 0.10  # 10% de descuento
        
    # +1 por la validación de precio
    if precio_base > 1000:
        descuento += 0.05  # 5% extra por compra grande

    precio_final = precio_base * (1 - descuento)
    return precio_final

# Uso del código
resultado = calcular_precio_final(1200, True, False)
print(f"El precio final es: ${resultado}")