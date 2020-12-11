import csv
class Contact:
    def __init__ (self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class ContactBook:
    def __init__ (self):
        self.contacts = []
    
    def add (self, name, phone, email):
        contact = Contact(name, phone, email)
        self.contacts.append(contact)
        self._save()
    def _save(self):
        with open ("ejercicio10.csv", "w") as f:
            writer = csv.writer(f, lineterminator="\r")
            writer.writerow(("name", "phone", "email"))
            for contact in self.contacts:
                writer.writerow((contact.name, contact.phone, contact.email))

    def show(self):
        for contact in self.contacts:
            self._show_contact(contact)

    def _show_contact(self, contact):
        print("\n------------------------------------------------")
        print(f"Nombre del contacto: {contact.name}")
        print(f"Telefono del contacto: {contact.phone}")
        print(f"Email del contacto: {contact.email}")

    def delete(self, command):
        for idx, contact in enumerate(self.contacts):
            if command.lower() == contact.name.lower():
                del self.contacts[idx]
                print("Contacto eliminado exitosamente")
                self._save()
                break
        else:
            print("No se encontro ese nombre de contacto.")
    
    def look(self, name):
        for contact in self.contacts:
            if name.lower() == contact.name.lower():
                print(f"\nNombre del contacto: {contact.name}")
                print(f"Telefono del contacto: {contact.phone}")
                print(f"Email del contacto: {contact.email}")
                break
        else:
            print("No se ha encontrado al contacto")

    def actualization(self, name):
        for idx, contact in enumerate (self.contacts):
                print(f"El contacto {contact.name} sufrira actualizaciones: ")
                name = str(input("\nEscribe el nombre del contacto: "))
                phone = str(input("Escribe el telefono del contacto: "))
                email = str(input("Escribe el mail del contacto: "))
                contact = Contact(name, phone, email)
                self.contacts.append(contact)
                self._save()
                break
        else:
            print("No se encontro al contacto")
                  
        
                

                

def run():
    
    contact_book = ContactBook()  
    
   with open ("ejercicio10.csv", "r") as f:
        reader = csv.reader(f)
        for idx, row in enumerate(reader):
            if idx == 0:
                continue
            elif row == []:
                continue
            else:
                contact_book.add(row[0], row[1], row[2])

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
                name = str(input("\nEscribe el nombre del contacto: "))
                phone = str(input("Escribe el telefono del contacto: "))
                email = str(input("Escribe el mail del contacto: "))

                contact_book.add(name, phone, email)
                
            elif command.lower() == "ac":
                name = str(input("\nEscribe el nombre del contacto que quiera actualizar: "))
                contact_book.actualization(name)
        
            elif command.lower() == "b":
                name = str(input("\nEscribe el nombre del contacto: "))
                contact_book.look(name)
        
            elif command.lower() == "e":
                command = str(input("\nIntroduce el nombre del contacto que quiere eliminar: "))
                contact_book.delete(command)
        
            elif command.lower() == "l":
                contact_book.show()

            elif command.lower() == "s":
                break
        except ValueError:
            pass



if __name__ == "__main__":
    run()