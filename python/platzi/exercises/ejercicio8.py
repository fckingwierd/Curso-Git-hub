
def run (second_answer):
    while True:
        try:
            print("No puedes ingresar letras o un numero mayor a 10")
            answer = int(input("Introduzca sus calificaciones para obtener un promedio, introduzca 'listo' si ha terminado: "))
            
            if answer > 10:
                while answer > 10:
                    print ("Los numeros deben ser menores o iguales a 10")
                    answer = int(input("Introduzca sus calificaciones para obtener un promedio, introduzca 'listo' si ha terminado: "))
            else:
                
                second_answer.append(answer)
                
        except ValueError:
            respuesta = input("Quieres terminar? responde con un y/n: ")
            if respuesta != "y" and respuesta != "n":
                while respuesta != "y" and respuesta != "n":
                    respuesta = input("Responde con un y/n: ")
            if respuesta == "n":
                pass
            else:
                break
    return second_answer
def prom_funtion(lista,iterator):
    for i in lista:
        iterator += i
    iterator = iterator / len(lista)
    return iterator

if __name__ == "__main__":
    second_answer = []
    iterator = float()
    lista = run(second_answer)
    prom = prom_funtion(lista,iterator)
    
    print(f"Tu promedio es de: {prom} ")
    



 
