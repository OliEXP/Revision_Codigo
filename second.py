print("=== Bienvenido al Juego de Trivia ===")
print("Responde correctamente a las preguntas. Tienes 3 vidas.\n")

vidas = 3
puntaje = 0

preguntas = {
    "¿Cuál es la capital de Francia?": "paris",
    "¿Cuánto es 5 * 6?": "30",   
    "¿Cuál es el color del cielo de día?": "azul",
    "¿Cuál es la raíz cuadrada de 81?": "9",
    "¿Cuántas caras tiene un cubo de Rubik 3x3?": "6",
    "¿Cuántos segundo hay en una hora?": "3600",
    "¿Cuál es la gravedad de la Tierra?": "9,8 m/s",
    "¿Cuál es la bandera que no es rectangular ni cuadrada?": "Nepal",
    "¿Cuál es la raíz cuarta de 6561?": "9",
    "¿Cuál es la raíz quinta de 7776": "6"

}

for pregunta, respuesta_correcta in preguntas.items():
    print(pregunta)
    respuesta_usuario = input("Tu respuesta: ")

    if respuesta_usuario.lower() == respuesta_correcta:  
        print("¡Correcto!\n")
        puntaje = puntaje + 1
    else:
        print("Incorrecto. La respuesta era:", respuesta_correcta, "\n")
        vidas = vidas - 1

    if vidas <= 0:
        print("😢 Te quedaste sin vidas.")
        break

print("Juego terminado.")
print("Tu puntaje fue:", puntaje)  
