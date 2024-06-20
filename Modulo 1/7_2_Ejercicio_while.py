numero_secreto = int(input("Usuario 1: Introduzca el número secreto (entre 1 y 10): "))
print("\n" * 50)
adivinado = False

while not adivinado:
    numero_usuario = int(input("Usuario 2: Introduce un número entre el 1 y 10: "))
    
    if numero_usuario == numero_secreto:
        print("Felicitaciones!!! has adivinado  el número.")
        adivinado = True
    else:
        print("Intenta de nuevo")