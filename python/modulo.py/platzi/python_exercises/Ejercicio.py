def pes_dol(ammount):
    arg_pesos = 0.017
    return arg_pesos * ammount
def dol_pel (ammount):
    dol = 71.78
    return dol * ammount

def run():
    print("C A L C U L A D O R A  D E  D I V I S A S ")
    print("Convierte dolares a pesos y viceversa")
    print("")

    respuesta = str(input("Quieres ingresar pesos o dolares?: "))

    if "dolares" == respuesta.lower():
        ammount = float(input("cuantos dolares quieres ingresar?: "))
        result = dol_pel(ammount)
        print (f"${ammount} dolares son {result} pesos argentinos..")
        
    elif "pesos" == respuesta.lower():
        ammount = float(input("Cuantos pesos quieres ingresar?: "))
        result = pes_dol(ammount)
        print (f"${ammount} pesos argentinos son {result} dolares.. ")
    else:
        pass
run()
