 # Paso 1: Solicitar al usuario las medidas de las piezas del mueble en cms

medidas_en_centimetros = float(input("Por favor, ingresar las medidas de la pieza del mueble (en cms) "))


# Paso 2:  Convertir las medidas de centimetros a pulgadas

medidas_en_pulgadas = medidas_en_centimetros / 2.54

# Paso 3: Mostrar las medidas convertidas al usuario

print("La medida de la pieza ingresada en pulgadas es: ", medidas_en_pulgadas)