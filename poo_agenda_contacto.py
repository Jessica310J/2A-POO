# EjemplosMundoReal_POO/agenda_contactos.py

# Clase Contacto: representa un contacto con nombre, teléfono y email
class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre            # Atributo nombre del contacto
        self.telefono = telefono        # Atributo teléfono
        self.email = email              # Atributo email

    def mostrar_contacto(self):
        # Método para mostrar la información del contacto
        return f"Nombre: {self.nombre}, Teléfono: {self.telefono}, Email: {self.email}"

# Continuación en agenda_contactos.py

class Agenda:
    def __init__(self):
        self.contactos = []             # Lista para almacenar objetos Contacto

    def agregar_contacto(self, contacto):
        # Añade un objeto Contacto a la lista
        self.contactos.append(contacto)

    def mostrar_todos(self):
        # Muestra todos los contactos almacenados
        return [contacto.mostrar_contacto() for contacto in self.contactos]

