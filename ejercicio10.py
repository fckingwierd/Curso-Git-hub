class Contact:
    def __init__ (self, name, phone, email):
        self.name = name
        self.phone = phone
        self.mail = email

class ContactBook:
    
    def __init__ (self):
        self.contacts = []
    
    def add (self, name, phone, email):
        print(f"Nombre: {name} Telefono: {phone} Email: {email}")


def run():
    
    contact_book = ContactBook()  

    while True:
        try:
            command = str(input("""
            (a)ñadir contacto
            (ac)tualizar contacto
            (b)uscar contacto
            (e)liminar contacto
            (l)istar contactos
            (s)alir
            Que deseas hacer?: """))

            if command.lower() == "a":
                name = str(input("Escribe el nombre del contacto: "))
                phone = str(input("Escribe el telefono del contacto: "))
                email = str(input("Escribe el mail del contacto: "))
                contact_book.add(name, phone, email)
                
            elif command.lower() == "ac":
                pass
        
            elif command.lower() == "b":
                pass
        
            elif command.lower() == "e":
                pass
        
            elif command.lower() == "l":
                pass

            elif command.lower() == "s":
                break
        except ValueError:
            pass



if __name__ == "__main__":
    run()