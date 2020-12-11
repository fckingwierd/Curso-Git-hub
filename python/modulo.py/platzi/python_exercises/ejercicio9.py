def carac_funt(lista):
    for letra in lista:
        if lista.count(letra) == 1:
            return letra 
        
    return False
                
if __name__ == "__main__":
    while True:
        character = str(input("Introduce una secuencia de caracteres: "))
        lista = list(character)
        result = carac_funt(lista)

        if not result:
            print("No hay caracteres no repetidos")
        else:
            print(f"El primer caracter no repetido es: {result} ")
        
        respuesta = input("Quieres ejecutar el programa de nuevo y/n?: ")
        if respuesta != "y" and respuesta != "n":
            while respuesta != "y" and respuesta != "n":
                respuesta = input("Debes introducir y/n: ")

        if respuesta == "n":
            break

        else:
            pass

