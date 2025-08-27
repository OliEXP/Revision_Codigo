import random

def instrucciones():
    print("=== Instrucciones ===")
    print("Debes adivinar el número secreto.")
    print("Dependiendo de la dificultad tendrás más o menos intentos.\n")

print("=== Bienvenido al Juego Adivina el Numero Pro ===")

while True:
    print("\nMenu Principal:")
    print("1. Jugar")
    print("2. Instrucciones")
    print("3. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        print("\nSelecciona dificultad:")
        print("1. Facil (1-10)")
        print("2. Medio (1-50)")
        print("3. Dificil (1-100)")

        dificultad = input("Opcion: ")

        if dificultad == "1":
            limite = 10
            intentos_maximos = 5
        elif dificultad == "2":
            limite = 50
            intentos_maximos = 10
        elif dificultad == "3":
            limite = 100
            intentos_maximos = 15
        else:
            print("Dificultad no valida.")
            continue

        numero_secreto = random.randint(1, limite)
        intentos = 0
        ganado = False

        while not ganado and intentos <= intentos_maximos:
            numero_jugador = int(input("Adivina el numero: "))

            if numero_jugador == numero_secreto:
                print("Ganaste")
                ganado = True
            elif numero_jugador > numero_secreto:
                print("Demasiado grande")
            elif numero_jugador < numero_secreto:
                print("Demasiado pequeno")

            intentos = intentos + 1

        if ganado == 0:
            print("Perdiste, el numero era", numero_secreto)

    elif opcion == "2":
        instrucciones()
    elif opcion == "3":
        print("Gracias por jugar")
        break
    else:
        print("Opcion incorrecta")
