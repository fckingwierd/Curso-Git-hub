def palindromo(word):
    word.lower()
    if word == word[::-1]:
        return True
    else:
        return False


if __name__ == "__main__":
    bolean = False
    while not bolean:
        word = str(input("Coloque una palabra: "))
        result = palindromo(word)
        if result:
            print(f"{word} es un palindromo")
        else:
            print (f"{word} no es un palindromo")
        respuesta = str(input("Quieres jugar de nuevo y/n?: "))
        if respuesta.lower() != "y" and respuesta.lower() != "n":
            while respuesta.lower() != "y" and respuesta.lower() != "n":
                respuesta = str(input("Tienes que escribir y/n: "))
        elif respuesta.lower() == "n":
            bolean = True
        else:
            pass

 