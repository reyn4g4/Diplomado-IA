"""
Escribir un programa que solicite dos numeros y luego imprima:
    1. La suma de los dos numeors
    2. La resta del primer numero menos el segundo
    3. El producto de dos numeros 
    4. El cubo de la suma de los dos numeros
    5. el cociente de la division del primer numero por el segundo
"""
b = float(input("ingrese un numero "))
c = float(input("ingrese un segundo numero "))

suma = b + c
resta = b - c
producto = b * c
cubo_de_la_suma = (b + c) ** 3
cociente = b / c if c != 0 else "Indefinido (división por cero)"

print("La suma de dos números b+c:", suma)
print("La resta del primer número menos el segundo b-c:", resta)
print("El producto de dos números b*c:", producto)
print("El cubo de la suma de los dos números (b+c)^3:", cubo_de_la_suma)
print("El cociente de la división del primer número por el segundo b/c:", cociente)

