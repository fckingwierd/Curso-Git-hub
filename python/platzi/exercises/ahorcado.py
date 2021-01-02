import random
i = 0
IMAGES = ["""                  +---+
                  |   |
                      |
                      |
                      |
                      |
                =========    """, 
          """                  +---+
                  |   |
                  O   |
                      |
                      |
                      |
                =========   """, 
           """                  +---+
                  |   |
                  O   |
                  |   |
                      |
                      |
                =========  """, 
           """                  +---+
                  |   |
                  O   |
                 /|   |
                      |
                      |
                =========  """, 
       """                  +---+
                  |   |
                  O   |
                 /|\\  |
                      |
                      |
                ========= """, 
        """                  +---+
                  |   |
                  O   |
                 /|\\  |
                 /    |
                      | 
                ========= """,
          """                  +---+
                  |   |
                  O   |
                 /|\\  |
                 / \\  |
                      |
                ========= """]
words = ["Teclado",
"Computadora",
"Escritorio", 
"Informacion",
"Estadistica",
"Resolucion",
"Caballo",
"Soga"]
        
def random_word():
    i_word = random.randint(0, len(words) - 1)
    return words[i_word]

def display_board(hidden_word,tries):
    print(IMAGES[tries])
    print ("")
    print(hidden_word)
    print("")
        
def ganador (hidden_word,current_letter,tries,boleano,letras):
    try:
        hidden_word.index("-")
    except ValueError:
        display_board(hidden_word, tries - 1)
        print("Felicidades! haz ganado")
        print(f"Numero de fallas: {tries} ")
        letras = letras + current_letter + "."
        print(f"letras usadas: {letras}")
        boleano = True
        if boleano:
            respuesta = str(input("Quieres jugar de nuevo y/n?: "))
            if respuesta != "y" and respuesta != "n":
                while respuesta != "y" and respuesta != "n":
                    respuesta = str(input("Responde con un y/n: "))
            elif respuesta == "n":
                return respuesta
            elif respuesta == "y":
                return respuesta
def perdedor (index_letters,hidden_word,tries,word,letras,current_letter):
        if tries == 7:            
            display_board(hidden_word, tries - 1)
            print("Lo siento! Haz perdido")
            print(f"Numero de fallas: {tries} ")
            letras = letras + current_letter + "."
            print(f"letras usadas: {letras}")
            print(f"La palabra correcta era: {word}")
            respuesta = str(input("Quieres jugar de nuevo y/n?: "))
            if respuesta != "y" and respuesta != "n":
                while respuesta != "y" and respuesta != "n":
                    respuesta = str(input("Responde con un y/n: "))
            if respuesta == "n":
                return respuesta
            else:
                return respuesta
def fallas(tries,index_letters,current_letter,letras):
    if len(index_letters) == 0:
        tries += 1
    if tries >= 1: 
        print(f"Numero de fallas: {tries} ")
        return tries
    if tries == 6:
            letras = letras + current_letter + "."
            print(f"letras usadas: {letras}")
def run ():
    respuesta = ""
    while True:
        boleano = False
        letras = ""
        iterador = 0
        tries = 0
        word = random_word()
        index_letters = []
        hidden_word = ["-"] * len(word)
        if respuesta == "n":
            break
        while True:
           
            display_board(hidden_word, tries)
                
            current_letter = str(input("Escoge una letra: "))

            for idx in range(len(word)):
                if word[idx] == current_letter.capitalize():
                    index_letters.append(idx)
            for idx in range(len(word)):
                if word[idx] == current_letter:
                    index_letters.append(idx)

            tries = fallas(tries,index_letters,current_letter,letras)
            if tries == 6:
                letras = letras + current_letter + ", "
                print(f"letras usadas: {letras}")
            
            if len(index_letters) != 0:
                for idx in index_letters:
                    hidden_word[idx] = current_letter
                index_letters = []

            respuesta = ganador(hidden_word,current_letter,tries,boleano,letras)   
            
            
            if "-" in hidden_word:
                respuesta = perdedor(index_letters,hidden_word,tries,word,letras,current_letter)      
    

            
            try:
                if tries < 6:
                    letras = letras + current_letter + ", "
                    print(f"Letras usadas: {letras} ")
            except TypeError:
                tries = 0
                if tries < 6:
                    letras = letras + current_letter + ", "
                    print(f"Letras usadas: {letras} ")

            if respuesta == "n":
                break
            if respuesta == "y":
                break
            
            iterador += 1
       


if __name__ == "__main__":
    
    run()
    
    