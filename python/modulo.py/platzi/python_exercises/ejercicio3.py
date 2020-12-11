import random 

def juego(lower,higher):
    intentos = 0
    number_found = False
    random_number = random.randint(lower,higher)
    while not number_found:
        numero = int(input("Ingrese un numero para adivinar: "))
        if numero < lower:
            print("Ingrese un numero dentro del campo que escribio anteriormente")
        elif numero > higher:
            print("Ingrese un numero dentro del campo que escribio anteriormente")
        elif numero == random_number:
            intentos += 1
            print(f"Felicidades! numero de intentos: {intentos}")
            number_found = True
        elif numero > random_number:
            intentos += 1
            print("El numero es mas pequeño")
        else:
            intentos += 1
            print("El numero es mas grande")

def numeros():
    lower = int(input("Ingresa el numero mas pequeño: "))
    higher = int(input("Ingresa el numero mas grande: "))

    if lower >= higher:
         while lower >= higher:
            print("Los numeros que ingresaste fueron incorrectos")
            lower = int(input("intentalo de nuevo: "))
            higher = int(input("Ingresa el numero mas grande: "))
    juego(lower,higher)
    
def iniciar():
    boleano = False
    while not boleano:
        numeros()
        respuesta = str(input("Quieres jugar de nuevo y/n?: "))

        if respuesta.lower() != "y" and respuesta.lower() != "n":
            while respuesta.lower() != "y" and respuesta.lower() != "n":
                respuesta = input("Tienes que escribir y/n: ")
        elif respuesta.lower() == "n":
            boleano = True
        else:
            pass

print("Bienvenido a este sutil juego")
iniciar()
        

        
