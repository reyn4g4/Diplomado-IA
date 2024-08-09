while True:
    try:
        dato_temp = float(input("Ingresa la temperatura del invernadero: "))
        break
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número.")


while True:
    try:
        dato_humedad = float(input("Ingresa la humedad del invernadero: "))
        break
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número.")


if dato_temp > 30 and dato_humedad >= 30:
    print("Se recomienda ventilación.")
elif dato_temp > 30 and dato_humedad < 30:
    print("Se recomienda riego y ventilación.")
elif dato_temp <= 30 and dato_humedad < 30:
    print("Solo se recomienda riego.")
else:
    print("No se recomiendan acciones.")