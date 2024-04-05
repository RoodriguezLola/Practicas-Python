import random

# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo", "inteligencia"]

# Elegir una palabra al azar
secret_word = random.choice(words)
# Número de fallos
max_attempts = 5 
cant= 0
won= False
# Lista para almacenar las letras adivinadas
guessed_letters = []

print("¡Bienvenido al juego de adivinanzas!")
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")

word_displayed = "_" * len(secret_word)
# Mostrarla palabra parcialmente adivinada
print(f"Palabra: {word_displayed}")

letters = []
level= input("Elegir un nivel de dificultad (Facil, Medio o Dificil): ")
if(level == 'Facil'):
    for letter in secret_word:
        if (letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u' or letter == 'ó'):
            letters.append(letter)
            guessed_letters.append(letter)
        else:
            letters.append("_")
    word_displayed = "".join(letters)
    print(f"Palabra: {word_displayed}")

else:
    if(level == 'Medio'):
        guessed_letters.append(secret_word[0])
        length= len(secret_word)
        guessed_letters.append(secret_word[length-1])
    for letter in secret_word:
        if letter == secret_word[0] or letter == secret_word[length-1]:
            letters.append(letter)
        else:
            letters.append("_")

    word_displayed = "".join(letters)
    print(f"Palabra: {word_displayed}")
    
#Permite el ingreso mientras tenga fallos
while (cant < max_attempts and not won):
    # Pedir al jugador que ingrese una letra
    letter = input("Ingresa una letra: ").lower()

    # Verificar si la letra ya ha sido adivinada
    if letter in guessed_letters:
        print("Ya has intentado con esa letra. Intenta con otra.")
        #cuenta los fallos si repite la letra
        cant += 1
        continue

    # Agregar la letra a la lista de letras adivinadas
    if(letter != "" and letter != '\n' and letter != " "):
        guessed_letters.append(letter)

    # Verificar si la letra está en la palabra secreta
    if (letter == "" or letter == '\n' or letter == " "): 
        print('Lo siento, No ha ingresado una letra')
    elif letter in secret_word:
        print("¡Bien hecho! La letra está en la palabra.")
    #Los fallos se cuentan cuando se equivoca de letra
    else:
        print("Lo siento, la letra no está en la palabra.")
        cant += 1

    # Mostrar la palabra parcialmente adivinada
    letters = []
    for letter in secret_word:
        if letter in guessed_letters:
            letters.append(letter)
        else:
            letters.append("_")

    word_displayed = "".join(letters)
    print(f"Palabra: {word_displayed}")
    # Verificar si se ha adivinado la palabra completa
    if word_displayed == secret_word:
        print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
        won= True

        break
else:
 print(f"¡Oh no! Has agotado tus {max_attempts} intentos.")
 print(f"La palabra secreta era: {secret_word}")