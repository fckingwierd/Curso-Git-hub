from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
class InstaBot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()
    def login(self):
        bot = self.bot
        bot.get("https://www.instagram.com")
        time.sleep(4)
        bot.find_element_by_class_name("KPnG0").click() 
        bot.find_element_by_id("email").send_keys(self.username)
        bot.find_element_by_id("pass").send_keys(self.password + Keys.RETURN)
        time.sleep(9)
    def hashtag(self):
        bot = self.bot
        bot.get("https://www.instagram.com/p/CFmsK4WDN0_/?hl=es-la")
        time.sleep(6)
    def download_image(self, lista, lista2, amount):
        bot = self.bot
        iterator = 0
        iterator2 = 0
        iterator3 = 0
        iterator4 = 0
        time.sleep(6)
        bot.find_element_by_class_name("Ypffh").click()
        while iterator <= amount:
            bot.find_element_by_class_name("Ypffh").send_keys("@" + lista[iterator2] + "_" + lista2[iterator3] + " ")
            iterator3 += 1
            iterator4 += 1
            if iterator3 == 98:
                iterator2 += 1
                iterator3 = 0
            time.sleep(10.2)
            if iterator4 == 6:
                bot.find_element_by_class_name("Ypffh").send_keys("@" + lista[iterator2] + "_" + lista2[iterator3] + Keys.RETURN)
                iterator4 = 0
    
            
#MENSAJES
lista = [
"Diego",
"Nicolas",
"Samuel",
"Alejandro",
"Daniel",
"Mateo",
"Angel",
"Matias",
"Gabriel",
"Tomas",
"David",
"Emiliano",
"Andres",
"Joaquin",
"Carlos",
"Alexander",
"Adrian",
"Lucas",
"Benjamin",
"Leonardo",
"Rodrigo",
"Felipe",
"Francisco",
"Pablo",
"Martin",
"Fernando",
"Isaac",
"Manuel",
"JuanPablo",
"Emmanuel",
"Emilio",
"Vicente",
"Eduardo",
"Juan",
"Javie",
"Jorge",
"Aaron",
"Jose",
"Erick",
"Luis",
"Cristian",
"Ignacio",
"Christopher",
"Jesus",
"Kevin",
"JuanJose",
"Agustin",
"JuanDavid",
"Simon",
"Joshua",
"Maximiliano",
"MiguelAngel",
"JuanSebastian",
"Bruno",
"Ivan",
"Gael",
"Miguel",
"Thiago",
"Jeronimo",
"Hugo",
"Ricardo",
"Antonio",
"Ian",
"Anthony",
"Pedro",
"Rafael",
"Jonathan",
"Esteban",
"JuanManuel",
"Julian",
"Mauricio",
"Oscar",
"Santino",
"Axel",
"Sergio",
"Guillermo",
"Matthew",
"Valentin",
"Bautista",
"Alvaro",
"Dylan",
"Marcos",
"Kimberly",
"Luciano",
"Mario",
"Cesar",
"Cristóbal",
"Luca",
"Iker",
"JuanAndres",
"Gonzalo",
"Roberto",
"Valentino",
"Facundo",
"Patricio",
"DiegoAlejandro",
"Josue",
"Franco"
]
lista2 = [
"Garcia",
"Gonzalez",
"Rodriguez",
"Fernandez",	 
"Lopez",	 
"Martinez",	 
"Sanchez", 
"Perez",	 
"Gomez",	 
"Martin",	 
"Jimenez",	 
"Ruiz",	 
"Hernandez",	 
"Diaz",	 
"Moreno",
"Muñoz",	 
"Alvarez",	 
"Romero",	 
"Alonso",	 
"GutiErrez",	
"Navarro", 
"Torres",	 
"DomInguez",	 
"Vazquez", 
"Ramos",	 
"Gil",
"Ramírez",	 
"Serrano", 
"Blanco",	 
"Molina",	 
"Morales",	 
"Suarez", 
"Ortega",	 
"Delgado",	 
"Castro", 
"Ortiz", 
"Rubio",	 
"Marin",	 
"Sanz",	 
"Nuñez",	
"Iglesias", 
"Medina",	 
"Garrido",	 
"Cortes",	 
"Castillo",	 
"Santos",	
"Lozano",	 
"Guerrero",	 
"Cano",	 
"Prieto",	
"Mendez",	
"Cruz",	
"Calvo",
"Gallego",	
"Vidal",	
"Leon",	
"Marquez",	
"Herrera",	
"Peña",	
"Flores",
"Cabrera",	
"Campos",	
"Vega",	
"Fuentes",	
"Carrasco",	
"Diez",	
"Caballero",	
"Reyes",	
"Nieto",	
"Aguilar",	
"Pascual",
"Santana",
"Herrero",
"Lorenzo",
"Montero",
"Hidalgo",
"Gimenez",
"Ibañez",
"Ferrer",
"Duran",
"Santiago",
"Benitez",	
"Mora",	
"Vicente",	
"Vargas",
"Arias",
"Carmona",	
"Crespo",	
"Roman",	
"Pastor",	
"Soto",	
"Saez",	
"Velasco",	
"Moya",	
"Soler",	
"Parra",
"Esteban",	
"Bravo",	
"Gallardo",	
"Rojas"	
]
ed = InstaBot ("thiagochiesa2010@hotmail.com","flamigera123")
ed.login()
ed.hashtag()
ed.download_image(lista, lista2, 30000)
