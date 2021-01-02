respuesta = input("Hola!, soy tu computadora personal, la cual esta autorizada para ayudarte a tener una mejor vida.\n\
	Pero antes de iniciar los procesos, necesito hacerte un par de preguntas. Estas listo?\n\
	Si o no?: ")
respuesta2 = " "
respuesta3 = " "
def yes_answer():
    print("Perfecto!, responde minuciosamente a las siguientes preguntas: ")

def no_answer():
	print("Cierre el programa inmediatamente")

def no_answer2(respuesta2):
	boleano2 = False
	respuesta2 = input ("Lamento decirle que es obligatorio. La respuesta es una forma etica para empezar.\nNo empezare hasta que contestes correctamente.\n\
		Si o no?: ")
	if respuesta2.lower() == "si":
		boleano2 = True
	if boleano2:
		yes_answer()
	else:
		no_answer()

def no_answer3(respuesta3):
	boleano3 = False
	respuesta3 = input("Porfavor, digite con un si o un no. La respuesta es una forma cordial para empezar.\n No empezare hasta que contestes correctamente.\n\
		Si o no?: ")
	if respuesta3.lower() == "si":
	     boleano3 = True
	if boleano3:
		yes_answer()
	else:
		no_answer()
if respuesta.lower() == "si":
	yes_answer()

elif respuesta.lower() == "no":
	no_answer2(respuesta2)

else:
	no_answer3(respuesta3)
	


